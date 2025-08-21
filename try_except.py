
#TRY AND EXCEPT
# astr = 'hello Bob'
# try:
#     istr = int(astr)
# except:
#     istr = -1
# print(istr)


#GRADER
# score = float(input("Enter Score: "))

# if score  <0.0 or score  >1.0:
#     print('error, please enter a valid number')

# if score >=0.9:
#     print('A')
# elif score >=0.8:
#     print('B')
# elif score >=0.7:
#     print('C')
# elif score >=0.6:
#     print('D')
# elif score <0.6:
#     print('F')

def computepay(h, r):
    if h <= 40:
        gross_pay = h * r
    else:
        overtime_hrs = h - 40
        gross_pay = (overtime_hrs * (r * 1.5) + (40 * r))
    return gross_pay

#input hours
hrs = float(input("Enter Hours: "))

#input rate
rate = float(input('Enter Rate: '))

#func called computepay()
p = computepay(hrs, rate )
print("Pay", p)