# import json

# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]'''

# info = json.loads(data)
# print('User count:', len(info))

# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])

    
import urllib.request
import json

# Prompt for the URL
url = input('Enter location: ') #
print('Retrieving', url)

# Read data from the URL
response = urllib.request.urlopen(url)
data = response.read().decode()
print('Retrieved', len(data), 'characters')

# Parse JSON
info = json.loads(data)

# Extract comments list
comments = info['comments']

# Initialize counters
count = 0
total = 0

# Loop through each item in the list
for item in comments:
    count = count + 1              # Increase the count for each comment
    total = total + item['count'] # Add this comment's count to the total


print('Count:', count)
print('Sum:', total)



    # XML PRACTICE
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
