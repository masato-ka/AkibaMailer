# -*- coding: utf-8 -*-

import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate


class MailSender:
    '''
    Mail Sender Object
    When your smtp server use tls, you should be set True to use_tls.
    '''
    password = ''
    username = ''
    use_tls = False

    def __init__(self, server, port):
        self.smtp_server = server
        self.smtp_port = int(port)

    def set_credential(self, username, password):
        """
        set password for mail server.

        :param String username: username for smtp server.
        :param String password: password for smtp server.
        :return: None
        """

        self.password = password
        self.username = username

    def send_mail(self, mail):
        """
        send mail to smtp server
        :param Mail mail: mail Object
        :return: None
        """
        self._do_send(mail, self.use_tls)


    def _do_send(self, mail, use_tls):
        """
        send mail method

        """
        smtp_server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        smtp_server.ehlo()
        if use_tls:
            smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(self.username, self.password)
        smtp_server.sendmail(mail.from_addr, 
                            [mail.to_addr], 
                            mail.get_mail_string())
        smtp_server.close()

class Mail:
    '''
    Mail Object
    '''

    charset = 'ISO-2022-JP'
    from_addr = ''
    to_addr = ''

    def __init__(self, body_text):
        self.msg = MIMEText(body_text.encode(self.charset), 
                            "plain", 
                            self.charset)
        self.msg["Date"] = formatdate(localtime=True)

    def set_header(self, subject):
        """
        
        """
        self.msg["Subject"] = Header(subject, self.charset)
        
    def set_from_addr(self, from_addr):
        self.msg["From"] = from_addr
        self.from_addr = from_addr

    def set_to_addr(self, to_addr):
        self.msg["To"] = to_addr
        self.to_addr = to_addr

    def set_charset(self, charset):
        self.charset = charset

    def get_from_addr(self):
        return seilf.msg["From"]

    def get_to_addr(self):
        return self.msg["To"]

    def get_mail_string(self):
        return self.msg.as_string()

