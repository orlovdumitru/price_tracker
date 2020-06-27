# from threading import Timer
from time import sleep

from domains.craig_price_tracker import CraigPrice
from domains.amz_price_tracker import AmazPrice
from domains.eba_price_tracker import EbaPrice


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


while looping_alert:
    timeout()
    sleep(elapse_time * 60)

# duration in seconds
# timer = Timer(how_often * 60, timeout)
# timer.start()

# wait to complete
# timer.join()