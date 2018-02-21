#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import smtplib for the actual sending function
import smtplib
import sys

# For guessing MIME type
import mimetypes

# Import the email modules we'll need
import email
import email.mime.application
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
secret = config.get('email', 'pass')

filename = str(sys.argv[1])
# Create a text/plain message
msg = email.mime.Multipart.MIMEMultipart()
msg['Subject'] = 'Email message from jenkins task' 
msg['From'] = 'auto.notification.as@gmail.com'
msg['To'] = 'andriy.shvorak@.plvision.eu'

# The main body is just another attachment
body = email.mime.Text.MIMEText(""" """)
msg.attach(body)

fp=open(filename,'rb')
att = email.mime.application.MIMEApplication(fp.read())
fp.close()
att.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(att)

# send via Gmail server
# NOTE: my ISP, Centurylink, seems to be automatically rewriting
# port 25 packets to be port 587 and it is trashing port 587 packets.
# So, I use the default port 25, but I authenticate. 
s = smtplib.SMTP('smtp.gmail.com')
s.starttls()
s.login('auto.notification.as@gmail.com',secret)
s.sendmail('auto.notification.as@gmail.com',['andriy.shvorak@plvision.eu'], msg.as_string())
s.quit()


