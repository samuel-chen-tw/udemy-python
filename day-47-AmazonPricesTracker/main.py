import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

MY_EMAIL = "samuel811215@gmail.com"
MY_PASSWORD = "zrcusgixpsqhgwul"
TO_LOMAN = "Loman.Cheng@taiwanlife.com"
TO_SAMUEL = "Samuel.chen@taiwanlife.com"
PRODUCT_URL = "https://www.amazon.com/-/zh_TW/dp/B0BCNKKZ91/ref=sr_1_1?crid=19J5AJ6AYXBRV&keywords=ps5&qid=1692600723&sprefix=ps5%2Caps%2C469&sr=8-1&th=1"
BUY_PRICE = 450

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    "Accept-Language": "zh-TW,zh-Hant;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "X-Requested-With": "XMLHttpRequest"
}

response = requests.get(url=PRODUCT_URL, headers=headers)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())
price_string = soup.find(name="span", class_="a-offscreen")
try:
    title = soup.find(id="productTitle").get_text().strip()
    price = float(price_string.get_text().split("$")[1])
    print(soup.prettify())
    print(price)
except AttributeError:
    print("Get the HTML fail, please try again")

if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        msg = MIMEText(message.encode("utf-8"), _charset="utf-8")
        msg['Subject'] = '有沒有專心上班?'
        msg['From'] = MY_EMAIL
        msg['To'] = TO_LOMAN
        connection.sendmail(
            from_addr=MY_PASSWORD,
            to_addrs=TO_LOMAN,
            msg=msg.as_string()
        )

