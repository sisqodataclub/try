import os
import streamlit as st
from google.auth import exceptions
from google.auth.credentials import Credentials
from googleapiclient.discovery import build

# Load the service account JSON key data from environment variable
service_account_json = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')

# Load credentials from the service account JSON key data
credentials = service_account.Credentials.from_service_account_info(
    service_account_json,
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)

# Create a service client using the credentials
service = build('sheets', 'v1', credentials=credentials)

st.write('hi')
