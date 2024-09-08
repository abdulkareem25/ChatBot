import streamlit as st

# Define the pages (Assuming other pages are already defined as before)
login_page = st.Page(page="views/login.py", title="Login", default=True)
home_page = st.Page(page="views/home.py", title="Home Page")
feature_1_page = st.Page(page="views/fileQnA.py", title="File Q&A")

# Setup Navigation
if not st.session_state.get('logged_in', False):
    pg = st.navigation({"Login": [login_page]})
else:
    pg = st.navigation(
        {
            "Home": [home_page],
            "File Q&A": [feature_1_page],
        }
    )

    # Adding the logout button at the bottom
    st.sidebar.button("Logout", key="logout", on_click=lambda: st.session_state.update({'logged_in': False}))

pg.run()
