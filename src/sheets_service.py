from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from gmail_service import SCOPES


def get_sheets_service():
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    service = build("sheets", "v4", credentials=creds)
    return service


def append_row(service, spreadsheet_id, sheet_name, row_data):
    body = {
        "values": [row_data]
    }

    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=f"{sheet_name}!A:E",
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()
