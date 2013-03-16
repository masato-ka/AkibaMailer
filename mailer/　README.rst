AkibaMailer
============

This python module is wapper of smtplib.
If you use this module, can easy send mail.

1. Install
-----------
Please run setup.py.
>python setup.py install


2. Using
----------


.. code-block:: Python

    from mailer import mailer
    
    #create Mail object
    mail = mailer.mail('test mail')
    mail.set_subject('subject of test mail')
    mail.set_from_addr('example@gmail.com')
    mail.set_to_addr('target@gmail.com')
    
    #create MailSender object
    mailsender = MailSender('smtp.gmail.com', 587)
    mailsender.set_credential('example@gmail.com', 'password')
    
    #If your smtp server use TLS, Please set parameter.
    mailsender.use_tls = True # Default False
    
    mailsender.send_mail(mail) #sending mail.

