import os
import requests
from local_settings import SUNLIGHT_API_KEY

filename = 'contact.csv'
outfile = open(filename, 'w')
outfile.write('state,name,chamber,district,party,email,phone\n')
outfile.close() #makes sure file is empty & has headers

key = SUNLIGHT_API_KEY
base_url = "http://openstates.org/api/v1/legislators/?apikey={key}&active=True"

results = requests.get(base_url.format(key=key))
results = results.json()


with open(filename, 'a') as outfile:
    for r in results:
        name = r['full_name']
        print(name)
        try:
            chamber = r['chamber']
        except KeyError:
            #this happens with weird peeps like tie-breaking lt govs.
            chamber = ""
        try:
            district = r['district']
        except KeyError:
            district = ""
        try:
            party = r['party']
        except KeyError:
            party = ""
        state = r['state']
        email = ''
        phone = ''
        for o in r['offices']:
            if 'email' in o and o['email']:
                email = o['email']
            if 'phone' in o and o['phone']:
                phone = o['phone']
        line = ','.join([state,name,chamber,district,party,email,phone])
        outfile.write(line+'\n')


