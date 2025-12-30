# SCRAPE USERS GOOGLE DOCS FOR CONTENT

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os
from scraper_utils import authenticate, list_all_google_docs, extract_doc_text


creds = authenticate()

drive_service = build("drive", "v3", credentials=creds)
docs_service = build("docs", "v1", credentials=creds)

docs = list_all_google_docs(drive_service)
print(f'found {len(docs)} Google Docs.')

documents = []

for f in docs:
    text = extract_doc_text(f["id"], docs_service)
    if not text:
        continue

    documents.append({
        "doc_id": f["id"],
        "title": f["name"],
        "text": text,
        "modified": f["modifiedTime"],
    })

print(f'extracted {len(documents)} docuemnts')
print(documents[27])