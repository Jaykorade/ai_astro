import secrets
import hashlib

from datetime import datetime
from datetime import timedelta
from config.settings import APP_URL
from sqlalchemy.orm import Session

from models.user import User

from models.password_reset_token import (
    PasswordResetToken
)

from emails.email_service import (
    send_reset_email
)

from auth.password_utils import (
    hash_password
)

import hashlib

from datetime import datetime

from models.user import User


def create_reset_request(
    db: Session,
    email: str
):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return False

    token = secrets.token_urlsafe(32)

    token_hash = hashlib.sha256(
        token.encode()
    ).hexdigest()

    reset_token = PasswordResetToken(
        user_id=user.id,
        token_hash=token_hash,
        expires_at=datetime.utcnow()
        + timedelta(minutes=30)
    )

    db.add(reset_token)

    db.commit()


    reset_link = (
    f"{APP_URL}/?reset_token={token}"
)

    send_reset_email(
        email,
        reset_link
    )

    return True

def reset_password(
    db,
    token,
    new_password
):

    token_hash = hashlib.sha256(
        token.encode()
    ).hexdigest()

    reset_record = db.query(
        PasswordResetToken
    ).filter(
        PasswordResetToken.token_hash
        == token_hash
    ).first()

    if not reset_record:
        return False

    if reset_record.used:
        return False

    if reset_record.expires_at < datetime.utcnow():
        return False

    user = db.query(User).filter(
        User.id == reset_record.user_id
    ).first()

    if not user:
        return False

    user.password_hash = hash_password(
        new_password
    )

    reset_record.used = True

    db.commit()

    return True