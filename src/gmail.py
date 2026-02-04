import os.path
from config import GMAIL_SCOPE, client_config

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def get_gmail(short=False, unread=False):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None

    query = "is:unread" if unread else ""
    limit = 5 if short else 10
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", [GMAIL_SCOPE])
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(client_config, [GMAIL_SCOPE])
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build("gmail", "v1", credentials=creds)
        results = (
            service.users()
            .messages()
            .list(userId="me", maxResults=limit, labelIds=["INBOX"], q=query)
            .execute()
        )
        messages = results.get("messages", [])

        if not messages:
            print("No messages found.")
            return
        print("Messages:")
        for msg in messages:
            msg_data = (
                service.users().messages().get(userId="me", id=msg["id"]).execute()
            )
            print("")
            print(f" :: ID: {msg_data['id']}")
            print(f"    Subject: {msg_data['snippet'][:100]}...")

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")
