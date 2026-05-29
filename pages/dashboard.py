import streamlit as st


def show():

    st.title("🔮 Dashboard")

    st.success(
        f"Welcome {st.session_state.user_name}"
    )

    st.write(
        "AI Astrology Platform"
    )

    st.write(
        "Upcoming Features:"
    )

    st.write(
        """
        ✅ Kundali Generation

        ✅ Dosha Analysis

        ✅ Dasha Analysis

        ✅ AI Astrologer Chat

        ✅ PDF Reports
        """
    )

    if st.button("Logout"):

        st.session_state.logged_in = False

        st.session_state.user_name = ""

        st.rerun()