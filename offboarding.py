import smtplib, ssl
import os
from email.message import EmailMessage
from pip._vendor import Github


user_email = "colovett@gmail.com"
user_pass = os.environ.get("PASSWORD")
contacts = ["charlielovett2025@u.northwestern.edu"]
git_users = ["charlielovett"]

def NUDM_remove(git_usernames):
    organization = Github.get_organization("NUDM")
    for git_username in git_usernames:
        organization.remove_from_membership(git_username)

    # slack remove


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
        <a href="https://join.slack.com/t/nudmappdevelo-ibm8455/shared_invite/zt-1iecb5jpf-Oc58EWLL9NZ5k0UwDR28aw" target="_blank">
            <button class="button button1">Join the Slack!</button>
        </a>
    </body>
    </html>
    """