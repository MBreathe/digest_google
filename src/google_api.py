import datetime

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def get_gcalendar(creds):
    try:
        service = build("calendar", "v3", credentials=creds)
        # Call the Calendar API
        now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=5,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])
        if not events:
            print("No upcoming events.")
            return
        print("Upcoming events:")
        # Prints the start and name of the next 5 events
        for event in events:
            start = (
                event["start"].get("dateTime", event["start"].get("date")).split("T")
            )
            start_date = start[0]
            start_time = start[-1].split("+")[0]

            end = event["end"].get("dateTime", event["end"].get("date")).split("T")
            end_date = end[0]
            end_time = end[-1].split("+")[0]
            print("")
            print(f"    :: ID: {event["id"]}")
            print(f"        TITLE: {event["summary"]}")
            print(f"        TIME: {start_date} {start_time} - {end_date} {end_time}")
            print(f"        LOCATION: {event["location"]}")

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")


def get_gmail(creds):
    try:
        # Call the Gmail API
        service = build("gmail", "v1", credentials=creds)
        results = (
            service.users()
            .messages()
            .list(userId="me", maxResults=10, labelIds=["INBOX"], q="is:unread")
            .execute()
        )
        messages = results.get("messages", [])

        if not messages:
            print("No unread messages.")
            return
        print("Messages:")
        for msg in messages:
            msg_data = (
                service.users().messages().get(userId="me", id=msg["id"]).execute()
            )
            print(f"    :: ID: {msg_data['id']}")
            for header in msg_data["payload"]["headers"]:
                if header["name"] == "From":
                    print(f"        FROM: {header['value']}")
                if header["name"] == "Subject":
                    print(f"        SUBJECT: {header['value']}")
            print("")

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")
