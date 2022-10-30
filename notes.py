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