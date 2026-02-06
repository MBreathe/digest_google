# Digest Google

A simple Python application that provides a daily digest by fetching unread emails from Gmail and upcoming events from Google Calendar.

## Features

- **Gmail Digest**: Lists up to 10 unread messages from your inbox, showing the sender and subject.
- **Calendar Digest**: Lists the next 5 upcoming events from your primary Google Calendar, including time and location.
- **OAuth2 Authentication**: Securely authenticates with Google APIs and stores credentials locally in `token.json` for subsequent runs.

## Prerequisites

- Python 3.13 or higher.
- A Google Cloud Project with Gmail and Calendar APIs enabled.
- OAuth 2.0 Client IDs (Desktop application) from the Google Cloud Console.

## Installation

This project uses `uv` for dependency management.

```bash
uv sync
```

## Configuration

The application requires several environment variables to be set in a `.env` file in the root directory. You can use the following template:

```env
# Google API Scopes
GMAIL_SCOPE=https://www.googleapis.com/auth/gmail.readonly
CALENDAR_SCOPE=https://www.googleapis.com/auth/calendar.readonly

# Google OAuth2 Client Configuration
CLIENT_ID=your_client_id
PROJECT_ID=your_project_id
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_SECRET=your_client_secret
REDIRECT_URIS=http://localhost
```

## Usage

Run the main script to see your digest:

```bash
python src/main.py
```

On the first run, a browser window will open asking you to log in to your Google account and authorize the application. Once authorized, a `token.json` file will be created locally to save your credentials.

## Project Structure

- `src/main.py`: Entry point of the application. Handles authentication and calls the API functions.
- `src/google_api.py`: Contains the logic for interacting with Gmail and Google Calendar APIs.
- `src/config.py`: Configuration loader that reads from the `.env` file.
- `pyproject.toml`: Project metadata and dependencies.
