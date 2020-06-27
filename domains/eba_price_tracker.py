# import requests
# from bs4 import BeautifulSoup
# import threading
# from urllib.parse import urljoin

import sys
sys.path.append('../')
from price_tracker.setup import MAX_PRICE, AMAZON_URL, HEADERS
from price_tracker.send_email import SendEmail



class EbaPrice(object):
    pass