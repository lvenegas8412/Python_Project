
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors (optional, but often needed)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))        # How many times to repeat following links
position = int(input('Enter position: '))  # Which link to follow (1-based index)

for i in range(count):
    print('Retrieving:', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')

    # Check if there are enough links
    if len(tags) < position:
        print('Not enough links on the page.')
        break

    # Get the link at the specified position (note: list is zero-indexed)
    url = tags[position - 1].get('href', None)

print('Last URL:', url)
