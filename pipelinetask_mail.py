#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import smtplib
from os.path import basename
from configparser import ConfigParser
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

config = ConfigParser()
config.read('config.ini')
secret = config.get('email', 'pass')
sendfrom = config.get('email', 'from')

def send_mail(send_from, send_to, subject, text, files=None,
              server='smtp.gmail.com'):
    assert isinstance(send_to, list)
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.starttls()
    smtp.login(send_from, secret)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--recipient', nargs='*', help='Recepients addresses', required=True)
    parser.add_argument('-s', '--subject', help='Subject')
    parser.add_argument('-m', '--message', help='Message')
    parser.add_argument('-a', '--attachment', nargs='*', help='Attachment')
    sendto = parser.parse_args().recipient
    subject = parser.parse_args().subject
    message = parser.parse_args().message
    attachment = parser.parse_args().attachment

    send_mail(sendfrom, sendto, subject, message, attachment)

