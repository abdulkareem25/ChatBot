import streamlit as st

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def sign_up(username, password):
    # Save credentials (For demonstration only, use a secure method in production)
    st.session_state.username = username
    st.session_state.password = password
    st.success("Sign-up successful. Please log in.")

def sign_in(username, password):
    # Check credentials
    if (username == st.session_state.get("username") and
        password == st.session_state.get("password")):
        st.session_state.logged_in = True
        st.success("Logged in successfully")
    else:
        st.error("Incorrect username or password")

if not st.session_state.logged_in:
    st.title("Login Page")

    option = st.selectbox("Choose Option", ["Sign In", "Sign Up"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if option == "Sign Up":
        if st.button("Sign Up"):
            sign_up(username, password)
    elif option == "Sign In":
        if st.button("Sign In"):
            sign_in(username, password)
else:
    st.write("You're already logged in!")
