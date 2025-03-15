from pyexpat import features
import requests
from bs4 import BeautifulSoup
import sys

#error handling 

if len(sys.argv > 1):
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED url!")

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, features = 'lxml')



