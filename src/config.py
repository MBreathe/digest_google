from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Extracting environment variables
SCOPES = [os.getenv("GMAIL_SCOPE"), os.getenv("CALENDAR_SCOPE")]

client_config = {
    "installed": {
        "client_id": os.getenv("CLIENT_ID"),
        "project_id": os.getenv("PROJECT_ID"),
        "auth_uri": os.getenv("AUTH_URI"),
        "token_uri": os.getenv("TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "redirect_uris": [os.getenv("REDIRECT_URIS")],
    }
}
