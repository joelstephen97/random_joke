import requests
import random

random_int = random.randint(0, 2164)
# print(random_int)
url = 'https://xkcd.com/'+str(random_int)+'/info.0.json'

resp = requests.get(url=url)
data = resp.json()
print(data["img"])
