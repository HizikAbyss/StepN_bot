import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time


def get_coins_info():
    ua = UserAgent()
    url = "https://coinmarketcap.com/currencies/green-satoshi-token/"
    time.sleep(1)
    r = requests.get(url=url, headers={'user-agent': f'{ua.random}'})

    soup = BeautifulSoup(r.text, "lxml")
    coin_data = soup.find_all("div", class_="sc-16r8icm-0 kjciSH priceSection")

    sol_gst = {}
    for coin in coin_data:
        coin_name = coin.find("h1", class_="priceHeading").text.strip()
        coin_price = coin.find_next("div", class_="priceValue").text.strip()

        article_id = url.split("/")[-2]

        sol_gst[article_id] = {
            "coin_name": coin_name,
            "coin_price": coin_price
        }

    url = "https://coinmarketcap.com/currencies/green-satoshi-token-bsc/"
    r = requests.get(url=url, headers={'user-agent': f'{ua.random}'})
    time.sleep(1)
    soup = BeautifulSoup(r.text, "lxml")
    coin_data = soup.find_all("div", class_="sc-16r8icm-0 kjciSH priceSection")

    bsc_gst = {}
    for coin in coin_data:
        coin_name = coin.find("h1", class_="priceHeading").text.strip()
        coin_price = coin.find_next("div", class_="priceValue").text.strip()

        article_id = url.split("/")[-2]

        bsc_gst[article_id] = {
            "coin_name": coin_name,
            "coin_price": coin_price
        }

    url = "https://coinmarketcap.com/currencies/green-metaverse-token/"
    r = requests.get(url=url, headers={'user-agent': f'{ua.random}'})
    time.sleep(1)
    soup = BeautifulSoup(r.text, "lxml")
    coin_data = soup.find_all("div", class_="sc-16r8icm-0 kjciSH priceSection")

    gmt = {}
    for coin in coin_data:
        coin_name = coin.find("h1", class_="priceHeading").text.strip()
        coin_price = coin.find_next("div", class_="priceValue").text.strip()

        article_id = url.split("/")[-2]

        gmt[article_id] = {
            "coin_name": coin_name,
            "coin_price": coin_price
        }

    url = "https://coinmarketcap.com/currencies/bnb/"
    r = requests.get(url=url, headers={'user-agent': f'{ua.random}'})
    time.sleep(1)
    soup = BeautifulSoup(r.text, "lxml")
    coin_data = soup.find_all("div", class_="sc-16r8icm-0 kjciSH priceSection")

    bnb = {}
    for coin in coin_data:
        coin_name = coin.find("h1", class_="priceHeading").text.strip()
        coin_price = coin.find_next("div", class_="priceValue").text.strip()

        article_id = url.split("/")[-2]

        bnb[article_id] = {
            "coin_name": coin_name,
            "coin_price": coin_price
        }

    url = "https://coinmarketcap.com/currencies/solana/"
    r = requests.get(url=url, headers={'user-agent': f'{ua.random}'})
    time.sleep(1)
    soup = BeautifulSoup(r.text, "lxml")
    coin_data = soup.find_all("div", class_="sc-16r8icm-0 kjciSH priceSection")

    sol = {}
    for coin in coin_data:
        coin_name = coin.find("h1", class_="priceHeading").text.strip()
        coin_price = coin.find_next("div", class_="priceValue").text.strip()

        article_id = url.split("/")[-2]

        sol[article_id] = {
            "coin_name": coin_name,
            "coin_price": coin_price
        }

    sol_gst.update(bsc_gst)
    sol_gst.update(gmt)
    sol_gst.update(bnb)
    sol_gst.update(sol)

    with open("Coins_info.json", "w") as file:
        json.dump(sol_gst, file, indent=4, ensure_ascii=False)


def main():
    get_coins_info()


if __name__ == '__main__':
    main()