import smtplib
import os
import mimetypes
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Email credentials (store these in .env file for security)
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")  # Sender's email
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # App password or actual password (if allowed)
SMTP_SERVER = "smtp.gmail.com"  # Change for other providers (e.g., Yahoo, Outlook)
SMTP_PORT = 587

def send_email(subject, body, to_emails, attachment_path=None):
    """
    Send an email with an optional attachment.
    
    :param subject: Email subject
    :param body: Email body
    :param to_emails: List of recipient email addresses
    :param attachment_path: Path to the file to attach (optional)
    """
    try:
        # Create an email message object
        msg = EmailMessage()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = ", ".join(to_emails)  # Send to multiple recipients
        msg["Subject"] = subject
        msg.set_content(body)  # Plain text body

        # Attach a file if provided
        if attachment_path:
            attachment_filename = os.path.basename(attachment_path)
            mime_type, _ = mimetypes.guess_type(attachment_path)

            # Default to 'application/octet-stream' if MIME type is not found
            mime_type = mime_type or "application/octet-stream"
            main_type, sub_type = mime_type.split("/", 1)

            # Read the file and attach it
            with open(attachment_path, "rb") as f:
                msg.add_attachment(f.read(), maintype=main_type, subtype=sub_type, filename=attachment_filename)

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login
            server.send_message(msg)  # Send email
            print("✅ Email sent successfully!")

    except Exception as e:
        print(f"❌ Error sending email: {e}")

# Example usage
if __name__ == "__main__":
    subject = "Automated Email with Attachment"
    body = "Hello,\n\nThis is a test email sent from a Python script.\n\nBest regards,\nYour Python Script"
    recipients = ["recipient@example.com"]  # Change this to actual recipient(s)
    attachment = "test.pdf"  # Change to a valid file path or set to None if not needed

    send_email(subject, body, recipients, attachment)
