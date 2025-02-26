# AutoMail

*Here's a Python script to send automated emails using SMTP, with support for attachments:*

- Sends an email using Gmail's SMTP server (can be modified for other providers).
- Supports attachments (PDFs, images, documents, etc.).
- Allows multiple recipients.
- Uses environment variables for security (optional).

## **Prerequisites**

1. Enable **Less Secure Apps** (if using Gmail) or create an **App Password** (recommended for security).
2. Install the required Python libraries:
    
    ```bash
    pip install smtplib email dotenv
    ```
    
3. Save your email credentials in a `.env` file for security.

## **How to Use Script**

1. **Set Up Environment Variables:**
    
    Create a `.env` file in the same directory and add:
    
    ```
    EMAIL_ADDRESS=your_email@gmail.com
    EMAIL_PASSWORD=your_app_password  # Use an App Password for better security
    ```
    
2. **Modify the script with your details:**
    - Replace `recipient@example.com` with actual recipients.
    - Provide a valid `attachment` file path or set it to `None`.
3. **Run the script:**
    
    ```bash
    python auto_mailer.py
    ```
    

## **Notes**

- If using **Gmail**, create an [App Password](https://myaccount.google.com/security) instead of using your actual password.
- For **Outlook**, change `SMTP_SERVER = "smtp.office365.com"` and use your email credentials.
- For **Yahoo Mail**, use `SMTP_SERVER = "smtp.mail.yahoo.com"`.