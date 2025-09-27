# import urllib.request
# import xml.etree.ElementTree as ET

# url = input('Enter location: ')
# if len(url) < 1 : 
#     url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

# print('Retrieving', url)
# uh = urllib.request.urlopen(url)
# data = uh.read()
# print('Retrieved',len(data),'characters')
# tree = ET.fromstring(data)

# counts = tree.findall('.//count')
# nums = list()
# for result in counts:
#     # Debug print the data :)
#     print(result.text)

# print('Count:', len(nums))
# print('Sum:', sum(nums))


import urllib.request
import xml.etree.ElementTree as ET

# Prompt for URL
url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'  # Default test URL

print('Retrieving', url)

# Read XML from URL
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

# Parse XML
tree = ET.fromstring(data)

# Find all <count> elements anywhere in the XML
counts = tree.findall('.//count')

# Initialize a list to store the numbers
nums = list()

# Extract and sum the count values
for result in counts:
    num = int(result.text)
    nums.append(num)

# Output results
print('Count:', len(nums))
print('Sum:', sum(nums))
