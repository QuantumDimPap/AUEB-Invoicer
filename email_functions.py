#Function for sending emails


def email(name,viesresult):

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    me = "" #sender's mail
    my_password = r"" #sender's password
    you = "" #receiver's mail

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Invoice Alert"
    msg['From'] = me
    msg['To'] = you

    html = '<html><body><p>Hello, an invoice for the company {} was received for payment. Vies validation: {} !</p><p>Thank you!</p></body></html>'.format(name,viesresult)
    part2 = MIMEText(html, 'html')

    msg.attach(part2)

    # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
    s = smtplib.SMTP_SSL('smtp.gmail.com')
    # uncomment if interested in the actual smtp conversation
    # s.set_debuglevel(1)
    # do the smtp auth; sends ehlo if it hasn't been sent already
    s.login(me, my_password)

    s.sendmail(me, you, msg.as_string())
    s.quit()