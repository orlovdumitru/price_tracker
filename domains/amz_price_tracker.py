
from selectorlib import Extractor
import requests
import json
from time import sleep
from bs4 import BeautifulSoup
import threading

import sys
sys.path.append('../')
from price_tracker.setup import MAX_PRICE, AMAZON_URL, HEADERS
from price_tracker.send_email import SendEmail


class AmazPrice(object):
    
    def __init__(self, search_for):
        self.url = AMAZON_URL + search_for
        self.price = MAX_PRICE
        self.headers = HEADERS

    def createExtractor(self):
        # Create an Extractor by reading from the YAML file
        e = Extractor.from_yaml_file('amazon-scraper/selectors.yml')
        return e


    def scrape(self, url):
        print(url)
        print(f"Downloading {url}")
        r = requests.get(url, headers=self.headers)

        if r.status_code > 500:
            if "To discuss automated access to Amazon data please contact" in r.text:
                print(f"Page {url} was blocked by Amazon. Please try using better proxies\n")
            else:
                print(f"Page {url} must have been blocked by Amazon as the status code was {status_code}\n")
            return None
        # Pass the HTML of the page and create
        print(r.text)
        return self.createExtractor().extract(r.text)


    def scraper(self):
        with open("amazon-scraper/urls.txt",'r') as urllist, open('amazon-scraper/output.jsonl','w') as outfile:
            for self.url in urllist.readlines():
                data = self.scrape(self.url) 
                if data:
                    json.dump(data,outfile)
                    outfile.write("\n")


    def getPrice(self):
        bike_url = "https://www.amazon.com/Longting-bicicleta-velocidades-bicicletas-plegables/dp/B089GM5F64/ref=sr_1_3?dchild=1&keywords=bike%2Bfor%2Bmen&qid=1593181704&sr=8-3&th=1&psc=1"

        response = requests.get(bike_url, headers=self.headers)
        if response.status_code > 500:
            print("Amazon is bocking your traffic \n")
            return 0

        soup = BeautifulSoup(response.content, "html.parser")
        try:
            title = soup.find(id="productTitle").get_text().strip()
            price = soup.find(id="priceblock_ourprice").get_text().strip()
        except:
            s_email = SendEmail("Amazon is checking if you are a bot", "Amazon blocked request")
            send_mail = s_email.sendEmail
            email_args = ('Amazon', bike_url)
            # create a separate thread to send email
            t = threading.Thread(target=send_mail, args=email_args)
            t.start()
            return -1
        return float(price[1:])


    def trackPrice(self):
        price = self.getPrice()
        if price == -1:
            print("Amazon blocked you")
            return -1
        if price > self.price:
            diff = price - self.price
            print(f"Price it is {diff} more than targeting")
        else:
            s_email = SendEmail("Price drop ")
            send_mail = s_email.sendEmail
            email_args = ('Amazon', self.url)
            # create separate thread to send email
            t = threading.Thread(target=send_mail, args=email_args)




def main():
    search_for = input("What are you looking for: \n")
    amz = AmazPrice(search_for)
    amz.getPrice()


if __name__ == "__main__":
    main()
