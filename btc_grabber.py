import urllib.request
import json
import time
import sys, select
from os import system

# To recieve a text message of price, change to desired values.
# Phone numbers are 10-digit numbers (ex: 5555555555)
phone_number = 0
btc_high = 290
btc_low = 225

# Replace currency code with desired abbreviation to change.
# Available codes listed at: https://blockchain.info/ticker
currency_code = 'USD'

# Checking user mode us autorun mode
print("If running manually press enter...")
for x in range(0, 5):
    print('-', end="", flush=True)
    i, o, e = select.select([sys.stdin], [], [], 1)
    if i:
        break

# # Getting exchange rate.
r = urllib.request.urlopen("https://blockchain.info/ticker").read()
data = json.loads(r.decode())
price = data[currency_code]['last']

# Output
if i:
    # Change $ to desired currency symbol to customize.
    print(end="")
    print("Current Bitcoin Exchange Rate: $" + str(price))
else:
    # Texting user if desired.
    if phone_number:
        if price > btc_high or price < btc_low:
            cmd = 'curl http://textbelt.com/text -d number=' + str(phone_number) + ' -d ' + '"message=' + 'Current Bitcoin Exchange Rate: ' + str(price) + '"'
            system(cmd)

