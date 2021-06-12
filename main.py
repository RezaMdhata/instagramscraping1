import requests
import json

url = 'https://www.instagram.com/graphql/query/?'

variable = {"shortcode":"CP-NWYwsQra","include_reel":True,"first":"24"}
headers = {"cookie": "ig_did=204366F2-39BB-4450-A883-B78FA25642EE"}
params = {
    "query_hash": "d5d763b1e2acf209d62d22d184488e57",
    'variables':json.dumps(variable)

}
r = requests.get(url, params=params)
user = r["data"]["shortcode_media"]

print(r)