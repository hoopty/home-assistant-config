#!/home/hass/hass/bin/python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-e', help='Entity name to check status')
args = parser.parse_args()

import requests
requests.packages.urllib3.disable_warnings()
url = 'https://localhost:8123/api/states/' + args.e
response = requests.get(url, verify=False)
try:
  state = response.json()['state']
except:
  state = None

if state == 'on':
  print('0')
elif state == 'off':
  print('100')
else:
  print('Unknown')
