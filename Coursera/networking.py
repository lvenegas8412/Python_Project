# import socket
# my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# my_sock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# my_sock.send(cmd)

# while True:
#     data = my_sock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# my_sock.close()

# ________URL READING FROM WEB

# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# for line in fhand:
#     print(line.decode().strip())

# ______BEATIFUL SOUP

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

# url  = input('Enter: ')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')

# tags = soup('a')
# # for tag in tags:
# #     print(tag.get('href', None))
# # print(tags)