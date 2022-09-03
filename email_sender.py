from email.message import EmailMessage
import ssl
import smtplib

sender = input('Enter your email adress (sender):')
password =  input('Enter your app password:')
receiver = input('Enter the receipients email adress:')


subject = input('Enter the email subject:')
body = input('Enter the email body:')


em = EmailMessage()
em['From'] = sender
em['To'] = receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, em.as_string())