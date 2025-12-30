
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/documents.readonly",
]
def authenticate():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds

def list_all_google_docs(drive_service):
    files = []
    page_token = None

    while True:
        response = drive_service.files().list(
            q="mimeType='application/vnd.google-apps.document' and trashed=false",
            fields="nextPageToken, files(id, name, modifiedTime)",
            pageSize=100,
            pageToken=page_token,
        ).execute()

        files.extend(response.get("files", []))
        page_token = response.get("nextPageToken")

        if not page_token:
            break

    return files

def extract_doc_text(doc_id, docs_service):
    doc = docs_service.documents().get(documentId=doc_id).execute()

    text = []
    for element in doc.get("body", {}).get("content", []):
        paragraph = element.get("paragraph")
        if not paragraph:
            continue

        for run in paragraph.get("elements", []):
            text_run = run.get("textRun")
            if text_run:
                content = text_run.get("content", "").strip()
                if content:
                    text.append(content)

    return "\n".join(text)
