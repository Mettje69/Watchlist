import streamlit as st
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="watchlist"
)
cursor = db.cursor()

# Set up Streamlit session state
class SessionState:
    def __init__(self):
        self.logged_in = False
        self.username = ""

session_state = SessionState()

# Registration form
def register_user(username, password):
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    db.commit()

# Login form
def authenticate(username, password):
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    if user:
        return True
    return False

# Main content
if session_state.logged_in:
    st.write(f"Welcome, {session_state.username}!")
    # Add your main content here
else:
    st.title("User Authentication")

    # Registration form
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    if st.button("Register"):
        register_user(new_username, new_password)
        st.success("Registration successful! Please log in.")

    # Login form
    if not session_state.logged_in:  # Display the login form only if the user is not logged in
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if authenticate(username, password):
                session_state.username = username
                session_state.logged_in = True
                st.success("Login successful!")
            else:
                st.error("Invalid username or password")

        if session_state.logged_in:
            st.write(f"Welcome, {session_state.username}!")
