from pyexpat import features
import requests
from bs4 import BeautifulSoup
import sys

#for regular expression
import re


#url: "https://ted.com/talks/ken_robinson_says_schools_kill_creativity"
#error handling 
'''
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter url!")
'''
print("Process started...")
url = "https://ted.com/talks/ken_robinson_says_schools_kill_creativity"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, features = 'lxml')

for val in soup.findAll("script"):
    if(re.search("talkPage.init", str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\\s]+)(mp4)", result).group("url")

mp4_url = result_mp4.split('"')[0]

print("Downloading the video form the url.... "+mp4_url)


fileName = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print("Storing the video in the file.... "+fileName)

r = requests.get(mp4_url)

with open(fileName, 'wb') as f:
    f.write(r.content)

print("Video downloaded successfully.")


