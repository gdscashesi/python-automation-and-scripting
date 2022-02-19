# Step 1
"""Find link to item you want to track"""

# Step 2
"""Generate email that will be used for notification"""

# Step 3
"""
Create API header
Use requests to get web info
"""

# Step 4
"""
Make soup
"""

# Step 5
"""Send email"""

import requests
from bs4 import BeautifulSoup
# import lxml
import smtplib as smtp
import os
from dotenv import load_dotenv

# loading environment variables
load_dotenv()

PRODUCT_URL = "https://www.jumia.com.gh/ps5-console-825gb-white-playstation-mpg441043.html"
test_email = os.environ.get('MY_EMAIL')
test_password = os.environ.get('MY_PASSWORD')

# making a request to page
header = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}
response = requests.get(url=PRODUCT_URL, headers=header)
web_data = response.text


# Making Soup
soup = BeautifulSoup(web_data, "html.parser")
# print(soup.title)

# Extracting the product title and price
product_title = soup.find(name="h1", class_="-fs20 -pts -pbxs").text
product_price = float(soup.find(name="span", class_="-b -ltr -tal -fs24").text.split(" ")[1].replace(",", ""))
# print(product_price)


# Sending the email id product price less than specified price
if product_price < 7000:
    with smtp.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=test_email, password=test_password)
        connection.sendmail(
            from_addr=test_email,
            to_addrs="chukwuexcel14@gmail.com",
            msg=f"Subject: Jumia Price Alert!\n\n{product_title} is now {product_price}. \n \
            Hurry to {PRODUCT_URL} to get it!"
        )
