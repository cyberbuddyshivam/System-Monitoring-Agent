# notifier.py
import os
from twilio.rest import Client

def send_sms(message: str) -> bool:
    """Send SMS alert. Returns True if sent successfully, False otherwise."""
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_FROM")
    to_number = os.getenv("ALERT_PHONE")

    if not all([account_sid, auth_token, from_number, to_number]):
        print("⚠️  SMS not configured (Twilio credentials missing)")
        return False

    try:
        client = Client(account_sid, auth_token)
        client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        return True
    except Exception as e:
        print(f"⚠️  Failed to send SMS: {e}")
        return False
