
import random
import re
import os
from credentials import *


MAX_PRICE = 200.00
MIN_PRICE = 10.00

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
TO_EMAIL = TO_EMAIL

IMG_PATH = "./images/"


def random_agent():
    '''
    https://www.networkinghowtos.com/howto/common-user-agent-list/?ref=hackernoon.com
    https://developers.whatismybrowser.com/useragents/explore/
    '''

    file = open('agents.txt', 'r')
    ag_text = file.read()
    file.close()
    
    path = "\n"
    agents = re.split(path, ag_text)
    idx = random.randint(0, len(agents)-1)
    return agents[idx]

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