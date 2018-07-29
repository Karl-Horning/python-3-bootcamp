import os
import requests
from pyfiglet import figlet_format
from termcolor import colored
from random import choice

random_color = choice(
    ('red',
     'green',
     'yellow',
     'blue',
     'magenta',
     'cyan',
     'white')
)
os.system('cls' if os.name == 'nt' else 'clear')
print(colored(figlet_format('Dad Joke 3000'), color=random_color))

url = 'https://icanhazdadjoke.com/search'
term = input('Let me tell you a joke! Give me a topic: ')

response = requests.get(
    url,
    headers={'Accept': 'application/json'},
    params={'term': term}
)

data = response.json()
total_jokes = data['total_jokes']
results = data['results']

if total_jokes == 0:
    print(f"I'm sorry, but I've got no jokes about {term}")
elif total_jokes == 1:
    print(f"I've got {total_jokes} joke about {term}. Here it is: ")
    print(choice(results)['joke'])
else:
    print(f"I've got {total_jokes} jokes about {term}. Here's one: ")
    print(choice(results)['joke'])
