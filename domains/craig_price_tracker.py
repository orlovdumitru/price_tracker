# https://www.crummy.com/software/BeautifulSoup/bs4/doc

import os
import requests
from bs4 import BeautifulSoup
import threading
from urllib.parse import urljoin

import sys
sys.path.append('../')

from price_tracker.setup import CRAIGSLIST_URL, CRAIGSLIST_IMG_URL, MAX_PRICE, MIN_PRICE, IMG_PATH
from price_tracker.send_email import SendEmail

class CraigPrice(object):

    def __init__(self):
        self.url = CRAIGSLIST_URL
        self.max_price = MAX_PRICE
        self.min_price = MIN_PRICE
        self.img_path = CRAIGSLIST_IMG_URL
        self.img_size = "_300x300.jpg"


    def getPrice(self, search_for):
        response = requests.get(f"{self.url}{search_for}")

        if response.status_code > 500:
            print("Craiglist is bocking your requests \n")
            return 0

        soup = BeautifulSoup(response.content, "html.parser")
        all_lis = soup.findAll("li", {'class': 'result-row'})
        filtered_items = ""
        idx = 1
        open_scraped_file = open("scraped_items/scraped_craig.txt", 'r+')
        scraped_text = open_scraped_file.read()

        for lis in all_lis:
            # set price
            price = lis.findAll("span", {"class":"result-price"})[0].get_text()[1:]
            if price.isnumeric():
                price = int(float(price))
            else:
                continue

            if price < self.max_price and price > self.min_price:
                # get title
                title = lis.find_all("a", class_ = "result-title hdrlnk")[0].get_text()
                # check if title in the file already
                existing_deal = f"{title} => {price}"
                if existing_deal in scraped_text:
                    continue
                else:
                    open_scraped_file.write(f"{existing_deal}\n")

                # get link
                link = lis.find("a", class_ = "result-title hdrlnk")
                link = link['href']
                # get immage
                image = ""
                try:
                    ids = lis.select("a")[0]['data-ids']
                    ids_img = (ids.split(":")[1]).split(",")[0]
                    image = urljoin(self.img_path, ids_img)
                    image += self.img_size
                except:
                    pass
                item = f'''
                    <b>{idx}</b>)
                    Title => <b><a href={link}>{title}</a></b><br>
                    Price => <b>${price}</b><br>
                    Image:<br>
                    <img src="{image}" alt="No image"><br><br>
                '''
                idx += 1
                filtered_items += item
            
        open_scraped_file.close()
            
        if len(filtered_items) > 0:
            s_email = SendEmail(filtered_items, "Craig list items")
            send_mail = s_email.sendEmail
            email_args = ('Craigslist',)
            # create a separate thread to send email
            t = threading.Thread(target=send_mail, args=email_args)
            t.start()


def main():
    craig = CraigPrice()
    looking_for = input("What are you looking for: \n")
    craig.getPrice(looking_for)


if __name__ == "__main__":
    main()