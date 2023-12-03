import random
import smtplib
import datetime as dt
import pandas

my_email = "all.junk.mails.my@gmail.com"
password = "jjbw dcrj tzun uydj"
email = "all.junk.mails.my@gmail.com"

reminder_time = dt.time(9, 0, 0)  # Set the reminder time at 9:00 AM

email_sent_today = False

while True:
    current_time = dt.datetime.now().time()

    # Compare the current time with the reminder time
    if current_time.hour == reminder_time.hour and current_time.minute == reminder_time.minute:
        # Check if email has already been sent today
        if not email_sent_today:
            data = pandas.read_csv("quotes.txt").values
            quotes_list = [quote[0] for quote in data]
            quote = random.choice(quotes_list)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject: Greeting\n{quote}")

            # Mark email as sent for the current day
            email_sent_today = True

    # Reset the email_sent_today flag at midnight
    if current_time.hour == 0 and current_time.minute == 0:
        email_sent_today = False
