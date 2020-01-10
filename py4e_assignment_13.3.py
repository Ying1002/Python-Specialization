import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
results = tree.findall(".//count")
print ("count:",len(results))
numlist=list()
for item in results:
    num=item.text
    Int=int(num)
    numlist.append(Int)
print ("sum:",sum(numlist))
