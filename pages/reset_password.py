import streamlit as st

from database.db import SessionLocal

from auth.password_reset_service import (
    reset_password
)


def show():

    token = st.query_params.get(
        "reset_token"
    )

    if not token:

        st.error(
            "Invalid reset link"
        )

        return

    st.title(
        "Reset Password"
    )

    password = st.text_input(
        "New Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button(
        "Reset Password"
    ):

        if password != confirm_password:

            st.error(
                "Passwords do not match"
            )

            return

        db = SessionLocal()

        success = reset_password(
            db,
            token,
            password
        )

        if success:

            st.success(
                "Password updated"
            )

        else:

            st.error(
                "Invalid or expired token"
            )