import requests
import json

raw_response = requests.get('https://api-v3.mbta.com/predictions?filter[route]=134&filter[stop]=9110&filter[direction_id]=1')
for entry in raw_response.json()['data']:
	print entry['attributes']
	break