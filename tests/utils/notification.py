import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

from app.logger.logger import logger


def send_email_with_report():
    report_path = os.path.join(os.path.dirname(__file__), '..', report_filename)
    report_path = os.path.abspath(report_path)

    message = Mail(
        from_email=os.getenv("SENDGRID_FROM_EMAIL"),
        to_emails=to_email,
        subject=subject,
        html_content=content
    )

    try:
        with open(report_path, "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data).decode()
            attachment = Attachment(
                FileContent(encoded),
                FileName(os.path.basename(report_path)),
                FileType("text/html"),
                Disposition("attachment")
            )
            message.attachment = attachment

        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        logger.error("Failed to send email: %s", e)
        return None
    
if __name__=="--main__":    
    # Example usage
    send_email_with_report()
    