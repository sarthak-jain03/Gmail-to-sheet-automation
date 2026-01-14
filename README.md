
# Gmail to Sheet Automation

This project is a Python-based automation system that reads real unread emails from my own Gmail account and logs them into a Google Sheet.
It uses the Gmail API and Google Sheets API with OAuth 2.0 authentication (no service accounts).

The system is designed to be idempotent, meaning re-running the script will never create duplicate rows.

## Objective
Each qualifying email is added as a new row in Google Sheets with the following fields:

| Column Name | Description                                      |
| ----------- | ------------------------------------------------ |
| From        | Sender email address                             |
| Subject     | Email subject                                    |
| Date        | Date & time received                             |
| Content     | Plain text email body                            |
| MessageID   | Unique Gmail message ID (used for deduplication) |



## High-Level Architecture




## Tech Stack
- Language: Python 3
APIs Used:
- Google Gmail API
- Google Sheets API
Authentication: OAuth 2.0 (Desktop App)

State Storage: Local JSON file



## Project Structure
```
gmail-to-sheets/
│
├── src/
│   ├── gmail_service.py
│   ├── email_parser.py
│   ├── sheets_service.py
│   ├── state_manager.py
│   ├── config.py
│   └── main.py
│
├── credentials/
│   └── credentials.json   
│
├── processed_ids.json     
├── token.json            
├── requirements.txt
├── .gitignore
├── README.md
└── proof/

```


## Setup Instructions

### 1. Google Cloud Configuration

- Create a Google Cloud Project
- Enable:
- Gmail API
- Google Sheets API
- Configure OAuth Consent Screen (External)
- Add your Gmail account as a Test User
- Create OAuth Client ID (Desktop App)
- Download credentials.json


### 2. Clone Repository
```sh
git clone https://github.com/sarthak-jain03/Gmail-to-sheet-automation
cd gmail-to-sheets
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```


### 4. Configure Google Sheet
- Create a new Google Sheet
- Add headers in Row 1: 
```
From | Subject | Date | Content | MessageID
```
- Copy the Spreadsheet ID
- Update src/config.py:
```
SPREADSHEET_ID = "YOUR_SPREADSHEET_ID"
SHEET_NAME = "Sheet1"
```


### 5. Run the Application
```
python src/main.py
```
- First run triggers OAuth consent
- Subsequent runs reuse the saved token

### OAuth Flow Explanation
- OAuth 2.0 Desktop App flow is used
- User authorizes access via browser
- Access and refresh tokens are stored in token.json
- Tokens are reused automatically
- No secrets are committed to Git

### Duplicate Prevention & State Persistence
Each Gmail email has a globally unique messageId.

Processed message IDs are stored in:
```
processed_ids.json
```

### Workflow
- Load previously processed IDs
- Fetch unread emails
- Skip emails already processed
- Append only new emails
- Save updated state
This ensures:
- No duplicate rows
- Safe re-runs
- Idempotent execution



### Email Processing Rules

Reads only:
- Inbox
- Unread emails
After processing:
- Emails are marked as read
Supports:
- Plain text emails
- Multipart emails
- HTML fallback where available

### Proof of Execution
The /proof/ folder contains:

- Gmail inbox screenshot (unread emails)
- Google Sheet screenshot (populated rows)
- OAuth consent screen screenshot



### Security Considerations
The following files are excluded using .gitignore:

- credentials.json
- token.json
- processed_ids.json
- .env
No secrets are committed.


### Challenges Faced

Challenge:
OAuth token initially lacked Google Sheets permissions.

Solution:
Regenerated the OAuth token with combined Gmail and Sheets scopes.

### Limitations

- HTML-only emails may have limited text extraction
- Single-user automation
- Manual OAuth setup required



### Author

Sarthak Jain

