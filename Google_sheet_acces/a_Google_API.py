from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/sqlservice.admin']
SERVICE_ACCOUNT_FILE = 'keyforgoogle.json'

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/documents']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID of a sample document.
DOCUMENT_ID = '14Of5eKIcuIKIZ2don7dpFFuzteIoroC4VNVBKkVNmIQ'

service = build('docs', 'v1', credentials=creds)

# Retrieve the documents contents from the Docs service.
document = service.documents().get(documentId=DOCUMENT_ID).execute()

print('The title of the document is: {}'.format(document.get('title')))

