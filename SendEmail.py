import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import re


password = 'oxzlvbxidlbmuyzp'
shipping_email = 'youscraphere@gmail.com'

class SendEmailCSV:

    def __init__(self, your_email):
        self.regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        self.your_email = your_email
        if re.search(self.regex, self.your_email):
            self.sendind_email_csv()
            return print(f"Archive csv sent to e-mail: {self.your_email}\n")
        else:
            raise Exception(f"Invalid e-mail, you typed: {self.your_email}")

    def sendind_email_csv(self):
        ## Body
        body_email = """
        <p>Hi, my pleasure, my name is <b>Matheus.</b></p>
        <p>Im Brazilian technology student and passion for inovation, if you recived this email, it's because my script sent the file content scraped public datasets
        <p> <b>I worked with scraping data for sites, if it is interest to you, view the table of values:
        Table of values:</b></p>
        <p>1 a 5.000 datasets: $ 5,00</p>
        <p>5.000 a 15.000 datasets: $ 10,00</p>
        <p>15.000 a 50.000 datasets: $ 25,00</p>
        <p>50.000 a 150.000 datasets: $ 50,00</p>
        <p>150.000 a 300.000 datasets: $ 100,00</p>
        <p>for more information, contact me</p>
        <p><b>Telegram: mts_frz</b> or Discord: https://discordapp.com/users/Matheus-Ferraz#3474</p>
        """
        ## Configuration the e-mail
        msg = MIMEMultipart()
        msg['Subject'] = 'Result of your web scrapy'
        msg['From'] = shipping_email
        msg['To'] = f'{self.your_email}'
        msg.attach(MIMEText(body_email, 'html'))

        arc_atch = "./output/amazon_products.csv"
        attachment = open(arc_atch, 'rb')

        att = MIMEBase('application', 'octet-stream')
        att.set_payload(attachment.read())
        encoders.encode_base64(att)

        att.add_header('Content-Disposition', 'attachment; filename=amazon_products.csv')

        msg.attach(att)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

class SendEmailJson:

    def __init__(self, your_email):
        self.regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        self.your_email = your_email
        if re.search(self.regex, self.your_email):
            self.enviar_email_json()
            print(f"Archive Json sent to e-mail: {self.your_email}\n")
        else:
            raise Exception(f"Invalid e-mail, you typed: {self.your_email}")            

    def enviar_email_json(self):
        ## Body
        body_email = """
        <p>Hi, my pleasure, my name is <b>Matheus.</b></p>
        <p>Im Brazilian technology student and passion for inovation, if you recived this email, it's because my script sent the file content scraped public datasets
        <p> <b>I worked with scraping data for sites, if it is interest to you, view the table of values:
        Table of values:</b></p>
        <p>1 a 5.000 datasets: $ 5,00</p>
        <p>5.000 a 15.000 datasets: $ 10,00</p>
        <p>15.000 a 50.000 datasets: $ 25,00</p>
        <p>50.000 a 150.000 datasets: $ 50,00</p>
        <p>150.000 a 300.000 datasets: $ 100,00</p>
        <p>for more information, contact me</p>
        <p><b>Telegram: mts_frz</b> or Discord: https://discordapp.com/users/Matheus-Ferraz#3474</p>
        """
        ## Configuration the e-mail
        msg = MIMEMultipart()
        msg['Subject'] = 'Result of your web scrapy'
        msg['From'] = shipping_email
        msg['To'] = f'{self.your_email}'
        msg.attach(MIMEText(body_email, 'html'))

        arc_atch = "./output/amazon_products.json"
        attachment = open(arc_atch, 'rb')

        att = MIMEBase('application', 'octet-stream')
        att.set_payload(attachment.read())
        encoders.encode_base64(att)

        att.add_header('Content-Disposition', 'attachment; filename=amazon_products.json')

        msg.attach(att)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
