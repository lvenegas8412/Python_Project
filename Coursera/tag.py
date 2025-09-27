
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


# Retrieve all the span tags
tags = soup('span')

total = 0
count = 0

for tag in tags:

    number = tag.contents[0]

    try:
        num = int(number)
        total += num
        count += 1
    except:
        continue

print('Count', count)
print('Sum', total)


import urllib.request
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the span tags
tags = soup('span')

total = 0
count = 0

for tag in tags:
    # Extract the text content of the span tag
    number = tag.contents[0]
    # Convert the text to integer
    try:
        num = int(number)
        total += num
        count += 1
    except:
        # If conversion fails, skip this tag
        continue

print('Count', count)
print('Sum', total)
