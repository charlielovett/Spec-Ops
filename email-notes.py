import smtplib, ssl
import os
import imghdr
from email.message import EmailMessage
import codecs
from github import Github

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


###
### HTML
###

# with codecs.open('testing.html', 'r', 'utf-8') as f:
#     html_string = f.read()

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
        <header>
            <h1>Join the Slack!</h1>
        </header>
        <a href="https://join.slack.com/t/nudmappdevelo-ibm8455/shared_invite/zt-1iecb5jpf-Oc58EWLL9NZ5k0UwDR28aw" target="_blank">
            <button style = "position:relative; left:50px"
                class="button button1">Link</button>
        </a>
    </body>
    </html>
    """


###
### SEND TO TERMINAL
###

#with smtplib.SMTP('localhost', 1025) as smtp:
#    smtp.send_message(msg)
#    print("Email has been sent")

###
### ATTACH JPEG
###

#files = [filenames...]

#for file in files:
#    with open(file, 'rb') as image:
#        file_data = image.read()
#        file_type = imghdr.what(image.name)
#        file_name = image.name
    
    # add files to message    
#    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

###
### ATTACH PDF
###

#files = ['stack-queue.pdf']

#for file in files:
#    with open(file, 'rb') as image:
#        file_data = image.read()
#        file_type = imghdr.what(image.name)
#        file_name = image.name
    
    # add files to message    
#    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)