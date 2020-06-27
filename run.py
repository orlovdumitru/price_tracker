from threading import Timer
import os

from domains.craig_price_tracker import CraigPrice
from domains.amz_price_tracker import AmazPrice
from domains.eba_price_tracker import EbaPrice
from tools import create_credentials, create_record_file


create_credentials()

search_in = (input("Search on Craigslist(c) | Ebay(e) | Amazon(a): \n")).lower()
looking_for = input("What are you looking for: \n")
how_often = input('How offten to get notification (ex: 1 minute => (1 m) | 1 hour  => (1 h) ): ')
elapse_time, units = how_often.split(" ")
looping_alert = False

if elapse_time.isnumeric():
    if units.lower() in ['m', 'minute']:
        elapse_time = int(elapse_time)
    elif units.lower() in ['h', 'hour']:
        elapse_time = int(elapse_time) * 60
    looping_alert = True
else:
    print("Incorect timing format")
    
craig = None
amaz = None
eba = None

if "craigslist" in search_in or "c" in search_in:
    craig = CraigPrice()
    create_record_file("scraped_craig.txt")

if "amazon" in search_in or "a" in search_in:
    amz = AmazPrice(looking_for)
    create_record_file("scraped_amaz.txt")
    
if "ebay" in search_in or "e" in search_in:
    eba = EbaPrice()
    create_record_file("scraped_eba.txt")


def timeout():
    if craig:
        craig.getPrice(looking_for)
    if amaz:
        amaz.getPrice()
    if eba:
        eba.getPrice(looking_for)


while looping_alert:
    # create thread duration in seconds
    timer = Timer(elapse_time * 60, timeout)
    timer.start()
    # wait to complete
    timer.join()