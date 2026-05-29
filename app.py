import streamlit as st

from pages import login
from pages import register
from pages import dashboard
from pages import forget_password

from pages import reset_password

st.set_page_config(
    page_title="AI Astrology",
    page_icon="🔮"
)


query_params = st.query_params

if "reset_token" in query_params:

    reset_password.show()

    st.stop()
    
if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if st.session_state.logged_in:

    dashboard.show()

else:

    page = st.sidebar.selectbox(
        "Menu",
        [
            "Login",
            "Register",
            "Forgot Password"
        ]
    )

    if page == "Login":

        login.show()

    if page == "Register":

        register.show()
    
    if page == "Forgot Password":
        forget_password.show()