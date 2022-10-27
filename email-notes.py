import smtplib, ssl
import os
import imghdr
from email.message import EmailMessage


# set variables
user_email = "colovett@gmail.com"
user_pass = os.environ.get("PASSWORD")
contacts = ["charlielovett2025@u.northwestern.edu", "hunterdisco2025@u.northwestern.edu"]
# IF MULTIPLE EMAILS:
#   contacts = [email1, email2, ...]
#   msg['To'] = ', '.join(contacts)

# set message
msg = EmailMessage()
msg['Subject'] = 'Hey'
msg['From'] = user_email
msg['To'] = ', '.join(contacts)
#msg.set_content('This is the body of the email')

###
### HTML
###

# with open('testing.html', 'r') as f:
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
            <h1>What's up</h1>
        </header>
        <a href="https://en.wikipedia.org/wiki/Supercentenarian" target="_blank">
            <button class="button button1">Link</button>
        </a>
        <p>Charlie Lovett</p>
    </body>
    </html>
    """

msg.add_alternative(html, subtype='html')

###
### SEND EMAIL
###

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(user_email, user_pass)
    print("Login success")
    smtp.send_message(msg)
    print("Email has been sent to ", contacts)








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