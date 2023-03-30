# Python program to add two numbers
'''a=int(input("enter 1 number:"))
b=int(input("enter 2 number:"))
c=a+b
print("sum of  number:",c)'''
# Maximum of two numbers in Python
'''a=12
b=2
if a>b:
    print("a is greaterthan:",a)
else:
    print("b is greaterthan:",b)'''
# Python Program for factorial of a number
'''n=int(input("enter a number:"))
f=1
for i in range(1,n+1):
    f=f*i
print(f)'''
n=int(input("enetr a number:"))
fac=1
i=1
while n>=i:
    fac=fac*i
    i=i+1
print(fac)

def faci(n):
    if n==1:
        return 1
    else:
        return (n*faci(n-1))
n=int(input("enetr a number:"))
if n<=0:
    print("no")
else:
    print(faci())