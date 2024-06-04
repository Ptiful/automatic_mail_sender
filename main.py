import os
import smtplib
import time
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
from random import randint
from tqdm import tqdm

load_dotenv()

sender_email = os.getenv("LOGIN")
app_password = os.getenv("APP_PASSWORD")

with open("PATH_TO_JSON.json", "r") as f:
    data = json.load(f)

for recipient_email in tqdm(list(data.keys()), desc="Sending emails"):
    print()
    company_name = data.pop(recipient_email)
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Data Engineer"
    body = f"""
    <html>
        <body>
            <p>Dear Hiring Manager,</p>

            <p>I am reaching out to express my interest in the Data Engineer position with {company_name}.</p>
            <p>As a recent graduate from BeCode and having completed an internship at Inoopa, I am excited about the opportunity to contribute to your team.</p>

            <p>Attached, you will find my CV which outlines my qualifications and experience. Here's a brief summary:.</p>

            <ul>
                <li><b>1 year experience working as a data engineer (Orange, Akkanto, Accenture use cases)</b></li>
                <li><b>Python / Pandas / Kubernetes / Airflow / Docker / CI/CD / ETL / AWS / AZURE</b></li>
                <li><b>Permanent employee</b></li>
            </ul>

            <p>I am eager to discuss how my background aligns with the needs of your team.</p>
            <p>Please let me know a convenient time for you, and I'll make myself available for a discussion.</p>

            <p>Thank you for considering my application. I look forward to the possibility of working together.</p>

            <p>You can also reach me on my phone : XXXXXXXXXXXXX</p>

            <p>Github : XXXXXXXXXXXX </p>
            <p>Linkedin : XXXXXXXXXXXXXX </p>

            <p>Best regards,<br>

            XXXXXX</p>
        </body>
    </html>
    """
    message.attach(MIMEText(body, "html"))

    attachment_path = "PATH_TO_ATTACHMENT"
    attachment_path_2 = "PATH_TO_ATTACHMENT2"

    with open(attachment_path, "rb") as attachment_file:
        attachment = MIMEBase("application", "octet-stream")
        attachment.set_payload(attachment_file.read())

    with open(attachment_path_2, "rb") as attachment_file_2:
        attachment_2 = MIMEBase("application", "octet-stream")
        attachment_2.set_payload(attachment_file_2.read())
    

    encoders.encode_base64(attachment)
    encoders.encode_base64(attachment_2)

    attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {os.path.basename(attachment_path)}",
    )
    attachment_2.add_header(
        "Content-Disposition",
        f"attachment; filename= {os.path.basename(attachment_path_2)}",
)

    message.attach(attachment)
    message.attach(attachment_2)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587  

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    server.login(sender_email, app_password)

    server.sendmail(sender_email, recipient_email, message.as_string())

    server.quit()

    print(f"Email with attachment sent successfully to {recipient_email}")

    with open("PATH_TO_JSON", "w") as file:
        json.dump(data, file)
    print("Json file has been updated!")
    print()

    time.sleep(randint(25,35))

print("All emails sent successfully.")
