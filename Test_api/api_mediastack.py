# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 14:13:22 2021

@author: Lenovo
"""

# Python 3
import http.client, urllib.parse
import json
my_key_mediastack="74713d7a61ca250397ba5e6b7b64b540"
ACCESS_KEY=my_key_mediastack
conn = http.client.HTTPConnection('api.mediastack.com')

params = urllib.parse.urlencode({
    'access_key': ACCESS_KEY,
    'categories': '-general,-sports', 
    'sort': 'published_desc',
    'limit': 50,            # maxi 100 compte gratuit
    })

conn.request('GET', '/v1/news?{}'.format(params))

res = conn.getresponse()
req = res.read()
req=req.decode('utf-8')
#media=eval(req)
#doc_mediastack=eval(req)
#print(doc_mediastack)
#print(type(media))

#media= json.dumps(req)
#data = json.loads(media)
print(req)

