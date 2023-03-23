import smtplib
import getpass
import imaplib
import email


def get_email_and_pass():
    # invisible in macos terminal
    email = getpass.getpass('Email: ')
    password = getpass.getpass('Password: ')

    return email, password


def s18_135_send():
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)  # or 465
    result = smtp_object.ehlo()
    print(result)

    # init tls
    result = smtp_object.starttls()
    print(result)

    email, password = get_email_and_pass()
    result = smtp_object.login(email, password)
    print(result)

    from_address = email
    to_address = email
    subject = input('Enter the subject line: ')
    message = input('Enter the body message: ')
    msg = 'Subject: ' + subject + '\n' + message

    result = smtp_object.sendmail(from_address, to_address, msg)
    print(result)

    smtp_object.quit()


def s18_136_receive():
    imap = imaplib.IMAP4_SSL('imap.gmail.com')

    email_addr, password = get_email_and_pass()
    imap.login(email_addr, password)

    print(imap.list())

    print(imap.select('inbox'))

    typ, data = imap.search(None, 'SUBJECT "NEW TEST PYTHON"')
    print(f'{typ} {data}')
    email_id = data[0]
    result, email_data = imap.fetch(email_id, '(RFC822)')
    print(email_data)

    raw_email = email_data[0][1]
    raw_email_string = raw_email.decode('utf-8')

    email_message = email.message_from_string(raw_email_string)
    for part in email_message.walk():
        if part.get_content_type() == 'text/plain':
            body = part.get_payload(decode=True)
            print(body)


if __name__ == '__main__':
    # s18_135_send()
    s18_136_receive()
