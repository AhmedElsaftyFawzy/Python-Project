import requests
from bs4 import BeautifulSoup
import smtplib

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

respond = requests.get("https://appbrewery.github.io/instant_pot/", headers=header)

soup = BeautifulSoup(respond.text, "html.parser")

price = float(soup.find(name="span", class_="a-offscreen").string[1:])

title = soup.find(id="productTitle").get_text().strip()

# Set the price below which you would like to get a notification
BUY_PRICE = 100

if price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\nhttps://appbrewery.github.io/instant_pot/.encode("utf-8")
        )