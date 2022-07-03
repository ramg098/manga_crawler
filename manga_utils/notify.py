import smtplib

def notify():
    try:
        smtp = smtplib.SMTP('smtp.gmail.com',587)
        smtp.starttls()
        mail = "ramg098@gmail.com"
        smtp.login(mail,"ekticwwfichyarrn")

        message = "new episode available "
        smtp.sendmail(mail,mail,message)
        smtp.quit()
    except Exception as ex: 
        print("Something went wrong....",ex)