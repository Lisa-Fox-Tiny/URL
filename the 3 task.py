from pprint import pprint

import requests

url = 'https://api.stackexchange.com/2.3/questions?fromdate=1686182400&todate=1686355200&order=desc&sort=activity&tagged=Python%20&site=stackoverflow'
resource = requests.get(url)
text = resource.json()
pprint(text)
