from pyexpat import features
import requests
from bs4 import BeautifulSoup
import sys

#for regular expression
import re

#error handling 

if len(sys.argv > 1):
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter url!")

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, features = 'lxml')

for val in soup.findAll("script"):
    if(re.search("talkPage.init", str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")

mp4_url = result_mp4.split('"')[0]



