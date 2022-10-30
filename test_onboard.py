import smtplib, ssl
import os
from email.message import EmailMessage
import Github


user_email = "colovett@gmail.com"
user_pass = os.environ.get("PASSWORD")
contacts = ["charlielovett2025@u.northwestern.edu"]

def NUDM_invite(emails, git_username):
    msg = EmailMessage()
    msg['Subject'] = 'Welcome to T&A!'
    msg['From'] = user_email
    msg['To'] = ', '.join(emails)
    msg.add_alternative(html, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(user_email, user_pass)
        print("Login success")
        smtp.send_message(msg)
        print("Email has been sent to ", emails)
    
    organization = Github.get_organization("Onboarding-Test-Organization")
    for email in contacts:
        organization.invite_user(git_username,email,"member")


html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
        .button {
            border: none;
            color: white;
            padding: 16px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            transition-duration: .4s;
            cursor: pointer;
        }

        .button1 {
            background-color: white; 
            color: black; 
            border: 2px solid #4CAF50;
        }

        .button1:hover {
            background-color: #4CAF50;
            color: white;
        }

        </style>
    </head>
    <body>
        <a href="https://join.slack.com/t/testworkspace-lwc9894/shared_invite/zt-1iqr11tfq-Nxt60Qg3sWObLa_STwcUcg" target="_blank">
            <button class="button button1">Join the Slack!</button>
        </a>
    </body>
    </html>
    """