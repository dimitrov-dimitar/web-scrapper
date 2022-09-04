import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from decouple import Config, RepositoryEnv


DOTENV_FILE = ".env.dev"
# DOTENV_FILE = "/home/dimitar/Desktop/web_scrapper/.env.prod"

config = Config(RepositoryEnv(DOTENV_FILE))


def send(msg, subject):
    credentials = {
        "username": config.get("EMAIL"),
        "password": config.get("PASSWORD"),
    }

    recipients = [config.get("EMAILS_ARR")]
    # 'petia.parkova@gmail.com'

    # Start connection
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Log in to the server
    server.login(credentials["username"], credentials["password"])

    # Build message
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = config.get("EMAIL")
    message["To"] = ", ".join(recipients)
    message_text = f'Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n{msg}'
    body = MIMEText(message_text)
    message.attach(body)

    # Send the mail
    server.send_message(message)
    print("Mail sent!")
