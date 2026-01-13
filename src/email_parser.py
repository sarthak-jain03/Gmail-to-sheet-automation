import base64


def get_header(headers, name):
    for h in headers:
        if h["name"].lower() == name.lower():
            return h["value"]
    return ""


def decode_base64(data):
    if not data:
        return ""
    decoded_bytes = base64.urlsafe_b64decode(data)
    return decoded_bytes.decode("utf-8", errors="ignore")


def extract_email_content(payload):
    """
    Handles:
    - plain text
    - multipart emails
    """
    if "parts" in payload:
        for part in payload["parts"]:
            if part.get("mimeType") == "text/plain":
                return decode_base64(part["body"].get("data"))
        
        for part in payload["parts"]:
            if "parts" in part:
                for sub in part["parts"]:
                    if sub.get("mimeType") == "text/plain":
                        return decode_base64(sub["body"].get("data"))
    else:
        return decode_base64(payload["body"].get("data"))

    return ""


def parse_email(service, message_id):
    msg = service.users().messages().get(
        userId="me",
        id=message_id,
        format="full"
    ).execute()

    headers = msg["payload"]["headers"]
    payload = msg["payload"]

    email_data = {
        "from": get_header(headers, "From"),
        "subject": get_header(headers, "Subject"),
        "date": get_header(headers, "Date"),
        "body": extract_email_content(payload)
    }

    return email_data
