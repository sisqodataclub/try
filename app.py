import os
import streamlit as st
from google.auth import exceptions
from google.auth.credentials import Credentials
from googleapiclient.discovery import build

# Load credentials from the environment variable
try:
    credentials = Credentials.from_authorized_user_info(
        os.environ['GOOGLE_APPLICATION_CREDENTIALS']
    )
except exceptions.DefaultCredentialsError:
    st.write("Failed to load credentials.")

# Now you can use the credentials to access Google services
service = build('sheets', 'v4', credentials=credentials)

# Example: Print the list of spreadsheets
spreadsheet_list = service.spreadsheets().list().execute()
st.write("Spreadsheets:")
for sheet in spreadsheet_list.get('files', []):
    st.write(f"- {sheet['name']}")
