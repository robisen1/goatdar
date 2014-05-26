

import twitter
import json
from pprint import pprint

json_data = open('twittersecret.json')
data = json.load(json_data)
pprint(data)
json_data.close()

dakey = data["CONSUMER_KEY"]

print(dakey)
