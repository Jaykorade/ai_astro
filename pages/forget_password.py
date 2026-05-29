import streamlit as st

from database.db import SessionLocal

from auth.password_reset_service import (
    create_reset_request
)


def show():

    st.title(
        "Forgot Password"
    )

    email = st.text_input(
        "Email"
    )

    if st.button(
        "Send Reset Link"
    ):

        db = SessionLocal()

        create_reset_request(
            db,
            email
        )

        st.success(
            "If account exists, "
            "reset link has been sent."
        )