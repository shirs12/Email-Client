import smtplib  # smpt protocol to send mails
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)  # 25 -> smpt port

server.ehlo()  # starting the server

with open('../utilities/password.txt', 'r') as f:  # saving password in another file
    password = f.read()

server.login('mail@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Name'
msg['To'] = 'testmail@spam.com'
msg['Subject'] = 'A Test'

with open('../utilities/message.txt', 'r') as f:  # mail body text in a txt file
    message = f.read()

msg.attach(MIMEText(message, 'plain'))  # attach the txt file to the mail

filename = '../utilities/coding.png'
attachment = open(filename, 'rb')  # rb -> read byte, for image

p = MIMEBase('application', 'octet-stream')  # the stream that process the image data
p.set_payload(attachment.read())
