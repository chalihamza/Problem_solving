# write a program to find sum of digits of a given number:
'''numbers=int(input("Enter a number:"))
sum=0
while numbers>0:
    sum=sum+numbers%10
    numbers=numbers//10
print("Sum of digits:", sum)'''
# write a program to find sum of square  digits of a given number:
'''numbers=int(input("Enter a number:"))
sum=0
while numbers>0:
    sum=sum+(numbers%10)*(numbers%10)
    numbers=numbers//10
print("sum of cube:", sum)'''

# write a program to find sum of cube  digits of a given number:
'''numbers=int(input("Enter a number:"))
cube=0
while numbers>0:
    cube=cube+(numbers%10)*(numbers%10)*(numbers%10)
    numbers=numbers//10
print("cube of number:", cube)'''
# Python Program to Check Armstrong Number
'''i = int(input("Enter a number:"))
cub = 0
org=i
while i > 0:
    cub = cub + (i % 10) * (i % 10) * (i % 10)
    i = i // 10
if org ==cub:
     print("number is armstrong:")
else:
    print("not armstrong number:")

print("\n Cube of a number:", cub)'''
# write a program to find product of cube  digits of a given number:
'''i=int(input("Enetr a number:"))
pr=1
while i>0:
    pr=pr*(i%10)
    i=i//10

print("product of a number:", pr)'''
# armstrong number for Nth term
n=int(input("Enter a number:"))
sum=0
tem=n
while tem>0:
    sum=sum