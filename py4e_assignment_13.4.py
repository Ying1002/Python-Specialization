import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retrieving', url)
data = urllib.request.urlopen(url).read().decode()

print('Retrieved', len(data), 'characters')
info = json.loads(data)
numlist=list()
stuff=info["comments"]
print ("count:",len(stuff))
for item in stuff:
    num=item["count"]
    Int=int(num)
    numlist.append(Int)
print ("sum:",sum(numlist))
