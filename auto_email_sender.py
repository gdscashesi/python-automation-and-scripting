# Importing required modules
import datetime as dt
import smtplib
from dotenv import load_dotenv
import os


# Step 1
"""Create a test gmail account"""

# Step 2
'''Make it less secure so we can use it to send emails.'''

# Step 3
'''Use datetime for date checking. Send email if date condition is met.'''


# Loading the variables into current environment
load_dotenv()

# Storing the environment variables
test_email = os.environ.get('MY_EMAIL')
test_email_password = os.environ.get('MY_PASSWORD')

# Setting the given time we want to send the email
send_time = dt.time(hour=14, minute=37)

# Email body to be sent
message_body = "Welcome to GDSC Python Session. I love you!"

# Sending the email
if dt.datetime.now().hour == send_time.hour and dt.datetime.now().minute == send_time.minute:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=test_email, password=test_email_password)
        connection.sendmail(from_addr=test_email,
                            to_addrs="chukwuexcel14@gmail.com",
                            msg=f"Subject: Your First Automatic Email\n\n{message_body}".encode("utf-8")
                            )





