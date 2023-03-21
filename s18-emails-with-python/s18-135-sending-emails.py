import smtplib
import getpass


def s18_135():
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)  # or 465
    result = smtp_object.ehlo()
    print(result)

    # init tls
    result = smtp_object.starttls()
    print(result)

    # invisible in macos terminal
    email = getpass.getpass('Email: ')
    password = getpass.getpass('Password: ')
    result = smtp_object.login(email, password)
    print(result)

    from_address = email
    to_address = email
    subject = input('Enter the subject line: ')
    message = input('Enter the body message: ')
    msg = 'Subject: '+subject+'\n'+message

    result = smtp_object.sendmail(from_address, to_address, msg)
    print(result)

    smtp_object.quit()


if __name__ == '__main__':
    s18_135()
