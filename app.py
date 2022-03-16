from cgitb import text
from bs4 import BeautifulSoup
import requests


#- Asking user to provide the desired URL
url_input = input("Enter your URL\n")

result = requests.get(url_input)
doc = BeautifulSoup(result.text, "html.parser")

#- Looking for the word "recipe" and returning what is found
recipe = doc.find_all(text="ingredients")
parent = recipe[0].parent
print(parent)

