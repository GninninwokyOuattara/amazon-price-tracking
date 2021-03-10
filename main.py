from datetime import datetime
import requests
from bs4 import BeautifulSoup
import smtplib
import os

TARGET_PRICE = float(os.environ.get("TARGET_PRICE"))
FROM = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")
TO = os.environ.get("TO")

url = "https://www.amazon.com/Instant-Pot-Programmable-Pressure-Steamer/dp/B01B1VC13K/ref=sr_1_1?dchild=1&keywords=instant+pot&qid=1615298576&sr=8-1"

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5',
            'From' : 'example@gmail.com'})

res = requests.get(url=url, headers=HEADERS)
soup = BeautifulSoup(res.text, "html.parser")
price = soup.select_one("#olpLinkWidget_feature_div > div.a-section.olp-link-widget > span > a > div > div > span.a-size-base.a-color-base").text
price_formatted = float(price[1::])

if price_formatted <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM, password=PASSWORD)
        connection.sendmail(from_addr=TO,to_addrs="idrissgouattara@gmail.com", msg=f"Subject:Price Notification\n\nThe project price is now {price} below, your target price. Buy Now!")
        connection.close()
else:
    print("higher price")



