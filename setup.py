
import random
# import re
import os
import json
from price_tracker.credentials import *


MAX_PRICE = 1200.00
MIN_PRICE = 500.00

CRAIGSLIST_URL = "https://chicago.craigslist.org/search/sss?sort=rel&query="
CRAIGSLIST_IMG_URL = "https://images.craigslist.org/"
EBAY_URL = ""
AMAZON_URL = "https://www.amazon.com/s?k="

# set envirinment variable
# os.environ["FROM_EMAIL"] = "email@email.com"
# retrive environment
# os.environ["FROM_EMAIL"]

FROM_EMAIL = FROM_EMAIL
PASSWORD = PASSWORD
PORT = 587
TO_EMAIL = TO_EMAIL


IMG_PATH = "./images/"


def random_agent():
    '''
    https://www.networkinghowtos.com/howto/common-user-agent-list/?ref=hackernoon.com
    https://developers.whatismybrowser.com/useragents/explore/
    '''
    file = open('agents.json', 'r')
    data = file.read()
    file.close()
    obj_data = json.loads(data)
    idx = random.randint(0, len(obj_data['agents'])-1)
    agent = obj_data['agents'][idx]["User-Agent"]
    return agent


HEADERS = {
    "User-Agent": random_agent(),
    "autority": "www.amazon.com",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "dnt": "1",
    # "upgrade-insecure-requests": "1",
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'sec-fetch-site': 'none',
    # 'sec-fetch-mode': 'navigate',
    # 'sec-fetch-dest': 'document',
    # 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}