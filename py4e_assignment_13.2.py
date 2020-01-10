
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
C=input("Enter count:")
count=int(C)
P=input("Enter position:")
pos=int(P)
i=1

# Retrieve all of the anchor tags
while i<=count:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    addresses=list()
    tags = soup('a')
    for tag in tags:
        URL=tag.get("href",None)
        addresses.append(URL)
    url=addresses[pos-1]
    i=i+1
    print("Retriving:",url)
    
    
    


