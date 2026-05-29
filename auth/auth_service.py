from sqlalchemy.orm import Session

from models.user import User

from auth.password_utils import hash_password,verify_password


def register_user(
    db: Session,
    full_name: str,
    email: str,
    password: str
):

    existing_user = db.query(User).filter(
        User.email == email
    ).first()

    if existing_user:
        return False

    user = User(
        full_name=full_name,
        email=email,
        password_hash=hash_password(password)
    )

    db.add(user)

    db.commit()

    return True


def login_user(
    db: Session,
    email: str,
    password: str
):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return None

    if verify_password(
        password,
        user.password_hash
    ):
        return user

    return None