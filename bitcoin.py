import sys
import requests

if not len(sys.argv)==2:
    sys.exit("Missing command-line argument")


try:
    num=float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    prices=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException():
    pass

pri=prices.json()
usd=pri["bpi"]
usd2=usd["USD"]
rate=usd2["rate"]

ratesep=rate.partition(".")
whole=(ratesep[0])
dec=float(ratesep[2])/10000
whole2=whole.replace(",","")


p1=float(whole2)
finrate=p1+dec

finrate=round(finrate,4)
fin=round(finrate*num,4)

fin = "{:,}".format(fin)

print(f"${fin}",end="")
