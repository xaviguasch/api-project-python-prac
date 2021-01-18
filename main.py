import requests
from random import choice
import pyfiglet

header = pyfiglet.figlet_format("DAD JOKE 3000!")
print(header)

topic = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": topic}
)

data = response.json()


num_jokes = data["total_jokes"]
results = data["results"]

if num_jokes == 1:
    joke = results["joke"]
    print(f"I've got one joke about {topic}. Here it is: \n {joke}")
elif num_jokes > 1:
    joke = choice(results)["joke"]
    print(f"I've got {num_jokes} jokes about {topic}. Here's one: \n {joke}")
else:
    print(f"Sorry, I don't have any jokes about {topic}! Please try again.")




