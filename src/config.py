from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Extracting environment variables
GMAIL_SCOPE = os.getenv("GMAIL_SCOPE")
CLIENT_ID = os.getenv("CLIENT_ID")
PROJECT_ID = os.getenv("PROJECT_ID")
AUTH_URI = os.getenv("AUTH_URI")
TOKEN_URI = os.getenv("TOKEN_URI")
AUTH_PROVIDER_X509_CERT_URL = os.getenv("AUTH_PROVIDER_X509_CERT_URL")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URIS = os.getenv("REDIRECT_URIS")

# Re-creating the credentials.json file
client_config = {
    "installed": {
        "client_id": CLIENT_ID,
        "project_id": PROJECT_ID,
        "auth_uri": AUTH_URI,
        "token_uri": TOKEN_URI,
        "auth_provider_x509_cert_url": AUTH_PROVIDER_X509_CERT_URL,
        "client_secret": CLIENT_SECRET,
        "redirect_uris": [REDIRECT_URIS],
    }
}
