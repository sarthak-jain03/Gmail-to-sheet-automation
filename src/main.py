from gmail_service import get_gmail_service, fetch_unread_emails
from email_parser import parse_email
from sheets_service import get_sheets_service, append_row
from state_manager import load_processed_ids, save_processed_ids
from config import SPREADSHEET_ID, SHEET_NAME


def main():
    gmail_service = get_gmail_service()
    sheets_service = get_sheets_service()

    processed_ids = load_processed_ids()
    messages = fetch_unread_emails(gmail_service)

    print(f"Unread emails found: {len(messages)}")

    new_processed = set(processed_ids)

    for msg in messages:
        message_id = msg["id"]

        
        if message_id in processed_ids:
            print("Skipping duplicate:", message_id)
            continue

        email = parse_email(gmail_service, message_id)

        row = [
            email["from"],
            email["subject"],
            email["date"],
            email["body"],
            message_id
        ]

        append_row(
            sheets_service,
            SPREADSHEET_ID,
            SHEET_NAME,
            row
        )

        print("Appended:", email["subject"])
        new_processed.add(message_id)

    
    save_processed_ids(new_processed)
    print("State saved. Processed IDs count:", len(new_processed))


if __name__ == "__main__":
    main()
