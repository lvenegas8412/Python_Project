# import re

# ##open and read text file
# data = open('Coursera/regex_real.txt')

# ##Create an empty list to store numbers from file
# numlist = list()

# ##Go through each line to find the numbers
# for line in data:
#     line = line.strip()

#     #find numbers 
#     digits = re.findall('[0-9]+', line)

#     #go through each list of numbers to turn into integers
#     for digit in digits:

#         #add them to list
#         numlist.append(int(digit))

# ##Sum up the total of the pulled numbers
# total = sum(numlist)
# print(total)

# ________URL READING FROM WEB

# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# for line in fhand:
#     print(line.decode().strip())

