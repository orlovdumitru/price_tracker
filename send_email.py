# https://realpython.com/python-send-email/

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

from price_tracker.setup import FROM_EMAIL, TO_EMAIL, PASSWORD, PORT


class SendEmail(object):

    def __init__(self, message, subject='No subject'):
        self.from_email = FROM_EMAIL
        self.password = PASSWORD
        self.to_email = TO_EMAIL
        self.message = message
        self.subject = subject
        self.port = PORT


    def sendEmail(self, page, url=''):
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = ','.join([self.to_email])
        msg['Subject'] = self.subject

        text = f"""
            {self.message}
            \n\n
            {url}
            """
        mem_text = MIMEText(text, "html")
        msg.attach(mem_text)
        
        # create secure context
        context = ssl.create_default_context()

        server = smtplib.SMTP(host="smtp.mail.com", port=self.port)
        server.ehlo()
        server.starttls(context=context) #secure connection
        server.ehlo()

        try:
            server.login(self.from_email, self.password)
            server.sendmail(self.from_email, msg['To'], msg.as_string())
            date_time = (datetime.now()).strftime("%a,(%d/%b/%Y) %X")
            print(f"{date_time} => Email sent ...")
        except Exception as e:
            print(f"unable to send email {e}")
        finally:
            server.quit()