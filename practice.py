
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

largest = None
smallest = None
nums = []
invalid_inputs = []
while True:
    num = input('Enter a Number: ')
    if num == 'done':
        break
    try:
        fval = int(num)
    except:
         print('Invalid input')
         continue
    
    if fval not in nums:
        nums.append(fval)
    for i in nums:
        if smallest is None:
            smallest = i
        elif i < smallest:
            smallest = i
        if largest is None:
            largest = i
        elif i > largest:
            largest = i

 
print('Maximun', largest)
print('Minimun', smallest)
    
    
   


