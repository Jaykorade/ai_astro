import streamlit as st

from database.db import SessionLocal

from auth.auth_service import login_user


def show():

    st.header("Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        db = SessionLocal()

        user = login_user(
            db,
            email,
            password
        )

        if user:

            st.session_state.logged_in = True

            st.session_state.user_id = user.id

            st.session_state.user_name = user.full_name

            st.success(
                f"Welcome {user.full_name}"
            )

            st.rerun()

        else:

            st.error(
                "Invalid Credentials"
            )