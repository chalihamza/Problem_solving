# Python program for Hello World
'''print("Hello world")'''
import calendar
import datetime
import math
from datetime import date

# Python program to add Two Numbers
'''a=int(input("enter 1 number:"))
b=int(input("enter 2 number:"))
c=a+b
print("sum of 2 number is :", c)'''
# Python program to subtract two numbers
# Python Program to Multiply Two numbers
# Python program for Arithmetic Operations
'''a=int(input("enter 1 number:"))
b=int(input("enter 1 number:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)'''
# Python program to print Calendar
'''y=int(input("enter year:"))
m=int(input("enter month:"))
print(calendar.month(y,m))'''
# Python Program to Calculate Cube of a Number
'''n=int(input("enter a number:"))
cube=n*n*n
cu=n**3
print("cube:", cube)
print("cube:", cu)'''
# Python program to find Largest of 2 Numbers
'''a=int(input("enter a 1 number:"))
b=int(input("enter a 2 number:"))
if a>b:
    print("largest number:", a)
else:
    print("largest  number:", b)'''
# Python program to find Largest of 3 Numbers

'''a = int(input("entre 1 number:"))
b = int(input("entre 2 number:"))
c = int(input("entre 3 number:"))
if a > b and a > c:
    print("a is largest:", a)
elif b > a and b > c:
    print("b is largest:", b)
else:
    print("c is largest:", c)'''
# Python program to Print Natural number 1 to N
# num = int(input("enter a last number:"))
'''i = 1
while i<=num:
    print(i, end=',')
    i = i + 1'''
'''for i in range(1,num+1):
    print(i)'''
# Python program for Leap Year
'''ya = int(input("Please Enter as you wish : "))

if ya % 400 == 0:
    print("%d is a Leap year" % ya)
elif ya % 100 == 0:
    print("%d is Not" % ya)
elif ya % 4 == 0:
    print("%d is a Leap year" % ya)
else:
    print("%d is Not" % ya)'''
# Python program to find Odd or Even

'''nu=int(input("enter a number:"))
if nu %2==0:
    print("even number", nu)
else:
    print("odd number:", nu)'''
# Python program to print Even Numbers from 1 to 100
'''n = int(input("enter a last number:"))
num = 1
while num <= n:
    if num % 2 == 0:
        print(num, end='  ')
    num = num + 1'''

'''n=int(input("enter last number:"))
for i in range(1,n+1):
    if i%2==0:
        print(i, end='  ')
''''''
n=int(input("enter last number:"))
for i in range(1, n+1, 2):
    print(i, end='  ')'''
# Python program to print Odd Numbers from 1 to 100
'''num=int(input("enter a last number:"))
i=1
while num>=i:
    if i % 2!=0:
        print(i, end='  ')
    i=i+1
'''
'''numbers = int(input("enter last number:"))
for i in range(1, numbers + 1):
    if i % 2 != 0:
        print(i, end=',')'''
# Python Program to Print Negative Numbers in a Range
'''numbers = int(input("Enter a number:"))
if numbers < 0:
    print("number is negative:", numbers)
else:
    print("its + number:", numbers)'''
# Python Program to Print Positive Numbers in a Range

'''numbers=int(input("Enter a number:"))
if numbers>0:
    print("number is +:", numbers)
else:
    print("not +", numbers)'''
# Python program to find Positive or Negative
'''num=int(input("Enter a number:"))
if num>0:
    print("number is +:", num)
else:
    print("number is -:", num)'''
# Python program to find Square of a Number
'''
numbers=int(input("Enter a numbers"))
square=numbers*numbers
squ=numbers**2
print(square)
print(squ)'''
# Python program to find Profit Or Loss
'''cost_price=int(input("Enter a cost price:"))
sale_price=int(input("Enter a sale price:"))
amount = sale_price-cost_price
if sale_price>cost_price:
    print("profit:",amount)
else:
    print("lose:",amount)'''

# Python program to find Square root of a Number
'''num=int(input("enter a number:"))
squ=math.sqrt(num)
print(squ)'''
# Python Program for simple interest
'''amount = int(input("enter a amount:"))
interest = int(input("Enter interest:"))
time = int(input("enter a time:"))
final = amount * time * interest / 100
final_py=amount+final
print("simple interest:", final)
print("simple full payment interest:", final_py)'''
# Python Program to find Compound Interest
'''amount = int(input("Enter a amount:"))
time = int(input("Enter a time:"))
interest = int(input("Enter a interest"))
com_inter = amount * (pow((1 + interest / 100), time))
ci=com_inter+amount
print(ci)
'''

# Python Program to find all divisors of an integer
'''number=int(input("Enter a number:"))
for i in range(1, number+1):
    if number % i==0:
        print(i)'''
'''nu = int(input("Enter a last number:"))
i = 1
while i <= nu:
    if nu % i == 0:
        print(i)
    i = i + 1'''
# Python program to check Number Divisible by 5 and 11
'''numbers=int(input("Enter a number:"))
if numbers %5== 0 and numbers %11==0:
    print("number is Divisible:", numbers)
else:
    print("NOT:", numbers)'''
# Python program to find Power of a Number
'''numbers=int(input("Enter a number:"))
expo=int(input("Enter exponent number:"))
power=math.pow(numbers,expo)
print("The Result of {0} power {1} ={2}".format(numbers,expo,power))'''
# using loop
'''numbers=int(input("Enter a number:"))
expo=int(input("Enter exponent number:"))
power=1
i=1
while i<=expo:
    power=power*numbers
    i=i+1
print(power)'''
# Python program for Multiplication Table
'''numbers = int(input("Enter a number:"))
for i in range(1, 11):
    print(numbers, "*", i, "=", numbers * i)'''
# Python Program to find roots of a Quadratic Equation
'''a = float(input("Enter the value of a:"))
b = float(input("Enter the value of b:"))
c = float(input("Enter the value of c:"))

delta = math.pow(b, 2) - (4 * a * c)
print(delta)
if delta > 0:
    x1 = (-b + math.sqrt(delta) / (2 * a))
    x2 = (-b - math.sqrt(delta) / (2 * a))
    # print(x1, x2)
    print("Squ root of: %f and %f" % (x1, x2))
elif delta == 0:
    x1 = x2 = (-b) / 2 * a
    print("There is a root:", x1, x2)
elif delta < 0:
    x1 = x2 = (-b) / 2 * a
    imaginary = math.sqrt(-delta) / (2 * a)

    print("No root:", x1,x2, imaginary)'''
# Python example to find Student Grade
'''english = int(input("Enter a marks of english:"))
mathes = int(input("Enter a marks of mathes:"))
physic = int(input("Enter a marks of physic:"))
computer = int(input("Enter a marks of computer:"))
chemestry = int(input("Enter a marks of chemestry:"))
total_marks=english+mathes+physic+computer+chemestry
percentage =(total_marks/500)*100
print("Total marks:", total_marks)
print("percentage:", percentage)
if percentage>=90:
    print("A grade")
elif percentage>=80:
    print("B grade")
elif percentage>=70:
    print("C grade")
elif percentage>=60:
    print("D grade")
elif percentage>=40:
    print("E grade")
else:
    print("Fail")
'''
# Python Program to Read 10 Numbers and Find their Sum and Average
'''total=0
for i in range(10):
    numbers=int(input("Enter a number\n"))
    total=total+numbers
average=total/10
print("sum of 10 number:", total)
print("average of 10 number:", average)'''
# Python Program to Print First 10 Natural Numbers
'''i=1
while i<=10:
    print(i)
    i=i+1
'''
'''for i in range(11):
    print(i)'''

# Python Program to Print First 10 Even Natural Numbers
'''for i in range(1,11):
    print(2*i)'''
'''i=1
while i<=10:
    print(2*i)
    i=i+1'''
# Python Program to Print First 10 Natural Numbers in Reverse
'''i=10
while i>=1:
    print(i)
    i=i-1
'''
'''for i in range(10,0,-1):
    print(i)'''
# Python Program to Print First 10 Odd Natural Numbers
'''odd=1
for i in range(10):
    print(odd,end=' ')
    odd=odd+2'''
'''i=1
while i<=10:
    print(i)
    i+=2'''
# Python program to Print Natural number 1 to N

'''numbers = int(input("Enter a last number:"))
i = 1
while i <= numbers:
    print(i, end=' ')
    i = i + 1'''
'''numbers = int(input("Enter a last number:"))
for i in range(1, numbers + 1):
    print(i)'''
# Python program to print Natural Numbers in Reverse Order
'''i = 10
while i>= 1:
    print(i, end=' ')
    i = i - 1'''
'''n=int(input("Enetr a number:"))
for i in range(n, 0, -1):
    print(i, end=' ')
'''
# Python Program to Find the Sum and Average Of Three Numbers
# a=int(input("Enetr 1 number:"))
'''b=int(input("Enetr 2 number:"))
c=int(input("Enetr 3 number:"))
su=a+b+c
avg=su/3
print("Sum of:", su)
print("Sum of:", avg)'''
# Python example to find Sum and Average of Natural Numbers
'''num = int(input("Enetr a last number:"))
sum = 0
for i in range(1, num + 1):
    print(i)
    sum = sum + i
avg = sum / num
print("sum of :", sum)
print("avg of :", avg)'''
# Python Program to Find Sum of 10 Numbers and Skip Negative Numbers
'''sum=0
for i in range(1,11):
    nu=int(input("Enter a number:\n"))
    if nu<0:
        continue
    sum=sum+nu
print("sum:", sum)'''
# Python Program to Find Sum of 10 Numbers until user enters Positive Numbers
'''sum=0
for i in range(1,11):
    num=int(input("enter number:\n"))
    if num<0:
        break
    sum=sum+num
print("kjsk:", sum)'''
# Python Program to Calculate Electricity Bill
'''unit=int(input("Enter a unit:"))
if unit>500:
    amount=unit*10
    tex=86
elif unit>=300:
    amount=unit*8
    tex=60
elif unit>=200:
    amount=unit*7
    test=50
else:
    amount=unit*5
    tex=10
total = amount+tex
print("your bil:", total)'''
# Python Program to Find Distance Between Two Points
'''x1 = int(input("Enter the First Point Coordinate x1  = "))
y1 = int(input("Enter the First Point Coordinate y1  = "))
x2 = int(input("Enter the Second Point Coordinate x2 = "))
y2 = int(input("Enter the Second Point Coordinate y2 = "))
x = math.pow((x2 - x1), 2)
y = math.pow((y2 - y1), 2)
distance = math.sqrt(x + y)
print("distance b/t two point:", distance)'''
# Python Program to Get Current Date and Time
'''tody=date.today()
print(tody)'''
'''tody = datetime.now()
dt=tody.strftime("%B%d%y%h%m%s%")
print(dt)'''

# Python Program to Make a Simple Calculator
'''print("Select operation you want to perform"
      " 1=add "
      "2=subtraction"
      "3=multiplication"
      "4=division"
      )
opt=int(input("choice operation from 1,2,3,4="))
n1=int(input("Enetr 1 number="))
n2=int(input("Enetr 2 number="))
if opt==1:
    print(n1,"+",n2,"=", n1+n2)
elif opt==2:
    print(n1,"-",n2, "=", n1-n2)
elif opt==3:
    print(n1, "*", n2, "=", n1*n2)
elif opt==4:
    print(n1, "/", n2, "=", n1*n2)
else:
    print("invalid:")'''
# Python Program to find Sum of Natural Numbers
'''numbers=int(input("Enetr a last number:"))
sum=0
for i in range(1, numbers+1):
    sum=sum+i
print(sum)
or
i=1
total=0
while i<=numbers:
    total=total+i
    i=i+1
print(total)'''
# Python Program to find Sum of Even Numbers
'''num=int(input("Enetr a number:"))
i=1
sum=0
while i<=num:
    if i % 2==0:
        print(i, end='  ')
        sum=sum+i
    i=i+1
print("sum of even:", sum)
or 

su=0
for i in range(1, num+1):
    if i % 2==0:
        print(i, end='  ')
        su=su+i
print(su)'''
# Python example to find Sum of Odd Numbers
'''numbers=int(input("Enetr a last number:"))
tot=0
for i in range(1, numbers+1):
    if i %2!=0:
        print(i, end='  ')
    tot=tot+i
print("total:", tot)'''
# Python example to find sum of Even and Odd Numbers
'''numbers=int(input("Enetr a last number:"))
even=0
odd=0
for i in range(1, numbers+1):
    if i % 2 ==0:
        even=even+i
    else:
        odd=odd+i
print("sum od even:", even)
print("sum od even:", odd)'''
#
# maximum = int(input(" Please Enter the Maximum Value : "))
# even_total = 0
# odd_total = 0
# maximum=int(input("Enetr last nu:"))
# for number in range(1, maximum + 1):
#     if (number % 2 == 0):
#         even_total = even_total + number
#     else:
#         odd_total = odd_total + number
# print(even_total)
# print(odd_total)
# Python Program to do Arithmetic Calculations using Functions
'''n1=int(input("Enter a number 1:"))
n2=int(input("Enter a number 2:"))
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1, n2):
    return n1*n2
def div(n1, n2):
    return n1/n2
def modu(n1,n2):
    return n1%n2
print("The addition=", add(n1,n2))
print("The substrication=", sub(n1,n2))'''
# Python Program to Count Number of Digits in a Number
'''number=int(input("Enter a number:"))
count=0
while number>0:
    number=number//10
    count=count+1
print("counting number:", count)'''
# Python Program to Print Fibonacci Series
'''numbers=int(input("Enetr a number:"))
x=0
y=1
z=0
while z<numbers:
    print(z, end='  ')
    x=y
    y=z
    z=x+y'''
'''numbers=int(input("\n Please enter a number:"))
fir=0
sec=1
for i in range(0, numbers):
    if i<=1:
        next=i
    else:
        next=fir+sec
        fir=sec
        sec=next
    print(next)'''

'''numbers=int(input("\n Please enter a number:"))
first=0
second=1
i=0
while i<numbers:
    if i<=1:
        next=i
    else:
        next=first+second
        first=second
        second=next
    print(next)
    i=i+1'''
'''
n=int(input("Enter a number:"))
first=0
second=1
i=0
while i<=n:
    if i<=1:
        next=i
    else:
        next=first+second
        first=second
        second=next
    print(next)
    i=i+1'''
# Python Program to Find the Sum of Fibonacci Series Numbers
'''n=int(input("Enter a number:"))
fir=0
sec=1
sum=0
i=0
while i<n:
    print(fir, end='  ')
    sum=sum+fir
    nex=fir+sec
    fir=sec
    sec=nex
    i=i+1
print("\n",sum)'''
# Python example to find Factors of a Number
'''n = int(input("Enetr a number:"))
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i = i + 1'''
'''n=int(input("Enter a number:"))
for i in range(1, n+1):
    if n % i ==0:
        print(i)'''
# Python example to find Factorial of a Number
'''n=int(input("Enter a number:"))
fac=1
i=1
while i<=n:
    fac=fac*i
    i=i+1
print(fac)'''
'''n=int(input("Enter a number:"))
fac=1
for i in range (1,n+1):
    fac=fac*i
print(fac)'''
# using recursion
'''def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
n=int(input("Enter a number:"))
if n<=0:
    print("factorial of a number less than 1 doesnot exists:")
else:
    print("Factorial of given number:", fact(n))'''
# Python program to print First Digit of a Number
'''n=int(input("Enter a number:"))
first_number=n
while first_number>=10:
    first_number=first_number//10
print("first digit", first_number)'''
'''n=123
fir_digit=n//100
print(fir_digit)'''
# Python program to print Last Digit in a Number
'''n=int(input("Enter a number:"))
last_digit=n%10
print(last_digit)'''
# Python program to find GCD of Two Numbers
'''a = int(input("Enetr 1 number:"))
b = int(input("Enetr 2 number:"))
i = 1
while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        c = i
    i = i + 1
print("\n hfc of {0} and {1}={2}".format(a, b, c))'''
'''using funcation
def HCF(a,b):
    if a>b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if a % i ==0 and b % i ==0:
            HCF=i
    return HCF
print("the hfc:", HCF(12,30))'''
# Python program to find LCM of Two Numbers
def LCM(a,b):
    if a>b:
        greatest=a
    else:
        greatest=b
    while(True):
        if greatest % a==0 and greatest % b==0:
            lcm=greatest
            break
        greatest=greatest+1
    return lcm
a=int(input("Enetr 1 number"))
b=int(input("Enetr 2 number"))
print("the lcm:", LCM(a,b))

