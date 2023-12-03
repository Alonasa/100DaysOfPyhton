import smtplib

my_email = "all.junk.mails.my@gmail.com"
password = "jjbw dcrj tzun uydj"
email = "all.junk.mails.my@gmail.com"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=email, msg="Subject:Greeting\nHello!")
    connection.close()
