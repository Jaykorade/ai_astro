import resend

from config.settings import RESEND_API_KEY

resend.api_key = RESEND_API_KEY


def send_reset_email(
    email: str,
    reset_link: str
):

    resend.Emails.send(
        {
            "from": "Astrology App <onboarding@resend.dev>",
            "to": [email],
            "subject": "Password Reset",
            "html": f"""
            <h2>Password Reset</h2>

            <p>Click below:</p>

            <a href="{reset_link}">
            Reset Password
            </a>
            """
        }
    )