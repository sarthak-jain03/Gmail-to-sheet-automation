from dotenv import load_dotenv
import os

load_dotenv()

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
SHEET_NAME = os.getenv("SHEET_NAME", "Sheet1")

if not SPREADSHEET_ID:
    raise ValueError("SPREADSHEET_ID not found in environment variables")
