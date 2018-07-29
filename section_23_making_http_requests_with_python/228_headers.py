# import requests
# url = 'https://icanhazdadjoke.com'

# response = requests.get(url, headers={'Accept': 'text/plain'})

# print(response.text)

import requests
url = 'https://icanhazdadjoke.com'

response = requests.get(url, headers={'Accept': 'application/json'})

data = response.json()

print(data['joke'])