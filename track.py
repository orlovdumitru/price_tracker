from threading import Timer
from time import sleep

from craig_price_tracker import CraigPrice
from amz_price_tracker import AmazPrice
from eba_price_tracker import EbaPrice


search_in = (input("Search on Craigslist(c) | Ebay(e) | Amazon(a): \n")).lower()
looking_for = input("What are you looking for: \n")
how_often = input('How offten to get notification (in minutes): ')
if how_often.isnumeric():
    how_often = int(how_often)

craig = None
amaz = None
eba = None

if "craigslist" in search_in or "c" in search_in:
    craig = CraigPrice()

if "amazon" in search_in or "a" in search_in:
    amz = AmazPrice(looking_for)
    
if "ebay" in search_in or "e" in search_in:
    eba = EbaPrice()



def timeout():
    if craig:
        craig.getPrice(looking_for)
    if amaz:
        amaz.getPrice()
    if eba:
        eba.getPrice(looking_for)


while True:
    timeout()
    sleep(how_often * 60)

# duration in seconds
# timer = Timer(how_often * 60, timeout)
# timer.start()

# wait to complete
# timer.join()