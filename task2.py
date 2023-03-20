import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class EmailWork:
 
    def __init__(self, _login, _password) -> None:
        self.connect = {'login': _login, 'password': _password}

    def send_message(self, _mail, _port, _recipients, _subject,):
        try:
            message = MIMEMultipart()
            message['From'] = self.connect['login']
            message['To'] = ', '.join(_recipients)
            message['Subject'] = _subject
            message.attach(MIMEText(message))

            sendmail_ = smtplib.SMTP(_mail, _port)
            sendmail_.ehlo()
            sendmail_.starttls()
            sendmail_.ehlo()
            sendmail_.login(self.connect['login'], self.connect['password'])
            result = sendmail_.sendmail(self.connect['login'], sendmail_, message.as_string())
            sendmail_.quit()
            return result
        except:
            return f'Fail to send: {Exception}'
            
    def recieve(self, _mail, _indox, _header=None):
        mail = imaplib.IMAP4_SSL(_mail)
        try:
            mail.login(self.connect['login'], self.connect['password'])
            mail.list()
            mail.select(_indox)

            criterion = '(HEADER Subject "%s")' % _header if _header else 'ALL'

            result, data = mail.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_string(raw_email)
            mail.logout()
            
        except: 
            return f'Fail to send: {Exception}'
        
if __name__ == '__main__':
    gmail = EmailWork('someuser@gmail.com', 'somepassword')
    print(gmail.sendmail(
        'smtp.gmail.com',
        587,
        ['oneuser@one.com', 'seconduser@two.com'],
        'Test message',
        'Body of test message'
    ))
    print(gmail.receive_mail('imap.gmail.com', 'inbox'))