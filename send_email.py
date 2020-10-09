import smtplib
from email.mime.text import MIMEText

def send_mail(mails, text, title):
    """
    Send email


    :param str[] | mails:
        The mail's array of recepients
    :param str | text:
        Mail's text
    :param str | title:
        Subject mail
    :param str | values:
        The values of restrict
    """
    try:

        smtp_ssl_host = 'email_smtp_ssl_host'
        smtp_ssl_port = 'email_smtp_ssl_port'
        username = 'email_username'
        password = 'email_password'


        from_addr = 'email_from_addr'
        to_addrs = mails


        message = MIMEText(text)
        message['subject'] = title
        message['from'] = from_addr
        message['to'] = ', '.join(to_addrs)


        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)
        server.sendmail(from_addr, to_addrs, message.as_string())
        server.quit()
    except:
        print('send_mail() - email_service', 'Error')