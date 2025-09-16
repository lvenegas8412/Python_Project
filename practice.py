
# #TRY AND EXCEPT
# astr = 'hello Bob'
# try:
#     istr = int(astr)
# except:
#     istr = -1
# print(istr)


# x = 5
# if  x == 5 :
#     print('Is 5')
#     print('Is Still 5')
#     print('Third 5')

#HOURS

# hrs = float(input("Enter hours: "))
# rate = 10.5   

# if hrs <= 40:
#     gross_pay = hrs * rate
# else:
#     overtime = hrs - 40
#     gross_pay = (40 * rate) + (overtime * (rate * 1.5))

# print(gross_pay)

# 5.2 Write a program that repeatedly prompts a 
# user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except 
# and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and 
# match the output below.

#EXAMPLE
# #largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#     print(num)

# print("Maximum", largest)

# largest = None
# smallest = None
# nums = []
# invalid_inputs = []
# while True:
#     num = input('Enter a Number: ')
#     if num == 'done':
#         break
#     try:
#         fval = int(num)
#     except:
#          print('Invalid input')
#          continue
    
#     if fval not in nums:
#         nums.append(fval)
#     for i in nums:
#         if smallest is None:
#             smallest = i
#         elif i < smallest:
#             smallest = i
#         if largest is None:
#             largest = i
#         elif i > largest:
#             largest = i

 
# print('Maximun', largest)
# print('Minimun', smallest)
    

# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"

# fh = open(fname)
# count = 0
# for line in fh:
#     while line.startswith('From'):
#         count = count +1
#         nline = line.split()
#         print(nline[1])
#         print(count)    

# print("There were", count, "lines in the file with From as the first word")

# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"

# fh = open(fname)
# count = 0
# for line in fh:
#     if line.startswith('From'):
#         count = count+1
#         nline = line.split()
        
# print(nline[1])

# print("There were", count, "lines in the file with From as the first word")

# #    -------------

# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)

# dic = {}

# for line in handle:
#     if line.startswith('From '):
#         words = line.split()
#         email = words[1]
#         dic[email] = dic.get(email, 0) +1

# topemail= None
# amount=None
# for word,count in dic.items():
#     if amount is None or count > amount:
#         amount = count
#         topemail=word
        
# print(topemail, amount)


# tu = ('h',1), ('j',7)
# result = ('h',1) > ('j',7)
# print(result)
# print(tu)

# d = {'v': 4, 'l': 10, 'm': 2}
# print(sorted(d.items()))
# for k,v in sorted(d.items()):
#     print(k,v)

# tmp = list()
# for k,v in d.items():
#     tmp.append((v,k))
# print(tmp)

# tmp = sorted(tmp, reverse=True)
# print(tmp)
