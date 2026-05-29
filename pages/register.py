import streamlit as st

from database.db import SessionLocal

from auth.auth_service import register_user


def show():

    st.header("Register")

    full_name = st.text_input(
        "Full Name"
    )

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register"):

        db = SessionLocal()

        success = register_user(
            db,
            full_name,
            email,
            password
        )

        if success:
            st.success(
                "Account Created"
            )
        else:
            st.error(
                "Email already exists"
            )