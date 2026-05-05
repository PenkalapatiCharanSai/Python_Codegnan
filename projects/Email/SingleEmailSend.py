from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#load dotenv file
import os
from dotenv import load_dotenv
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSKEY = os.getenv("SENDER_PASSKEY")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def SingleEmailSender(to_email:str, subject:str, body:str):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))


    try:
        #Create SMTP Server
        server = SMTP(SMTP_SERVER, SMTP_PORT)
        #start server
        server.starttls()
        #login to server
        server.login(SENDER_EMAIL, SENDER_PASSKEY)
        #send email
        server.sendmail(from_addr=SENDER_EMAIL, to_addrs= to_email, msg = msg.as_string())

        #close server
        server.quit()
        print(f"Email sent successfully to  {to_email}")
    except:
        print(f"Unable to send email {to_email}")


to_email = input("Enter receiver email address:")
subject = input("Enter the subject:")
body = input("Enter email-body:")

#calling the function i.e Single email sender function
SingleEmailSender(to_email = to_email, subject = subject, body = body)


    

