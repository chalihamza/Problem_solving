# Python | Largest, Smallest, Second Largest, Second Smallest in a List
from math import dist


def find_li(lis):
    # length=len(lis)
    lis.sort()
    print("Second small number:", lis[1])
    print("second big number:", lis[-2])


lis = [1, 2, 5, 3, 5, 7, 8, 9]
large = find_li(lis)

# replace first character with last
'''def change(s):
    first, *middel, last = s.split()
    print(last, *middel, first)


s = str(input("ENter a string:"))
change(s)
'''

# d={"A":['a',3], "B":['b',2],"C":['c',5],"D":['d',4]} sort this list with second value and output={"B":['b',2],"A":['a',3],"D":['d',4],"C":['c',5]}

'''d = {"A": ['a', 3], "B": ['b', 2], "C": ['c', 5], "D": ['d', 4]}
sort=dict(sorted(d.items(),key=lambda x:x[1][1]))
print(sort)'''

# Python program to check Palindrome or Not
'''def palin(s):
    tem=s[::-1]
    if s==tem:
        print("Palindrome")
    else:
        print("Not Palindrome")
s=str(input("Enetr a string"))
palin(s)'''

# using indexing
'''def palin(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n - i - 1]:
            return False
    return True'''
# using join
'''def palin(s):
    tem=''.join(reversed(s))
    if s==tem:
        return True
    else:
        return False'''
# using while loop
'''def palin(s):
    n=len(s)
    first=0
    last=n-1
    while first<last:
        if s[first]==s[last]:
            first=first+1
            last=last-1
        else:
            return False
    return True
s = str(input("Enetr a string"))
print(palin(s))
'''

# Python Program to Check a Number is Palindrome or Not
'''i = int(input("Enter a number:"))
n = i
rev = 0
while i > 0:
    rev = (rev * 10) + i % 10
    i = i // 10
if n == rev:
    print("palindrom")
else:
    print("not")'''
# using slicing
'''num=121
revs=int(str(num)[::-1])
if num==revs:
    print("p")
else:
    print("n")'''

# Python Program to Print Fibonacci Series
'''def febon(n):
    first=0
    second=1
    print(first)
    while second<n:
        print(second)
        c=first+second
        first=second
        second=c
febon(50)
print()'''
# without using 3rd variable
'''def feb(n):
    f,s=0,1
    print(f)
    while s<n:
        print(s)
        f,s=s,f+s
feb(150)'''

# using for loop

'''n=int(input("enet a number:"))
a,b=0,1
for i in range(n):
    print(a,end='')
    a,b=b,a+b'''

# using recursion
'''def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
n=10
if n<=0:
    print("invalid")
else:
    for i in range(n):
        print(fib(i))'''

# write python program input=aawweefffkkkk output=a2w2e2f3k4
'''st = input("enter a string:")
ch = {}
for i in st:
    if i in ch:
        ch[i] = ch[i] + 1
    else:
        ch[i] = 1
print(ch)
out = ""
for i, count in ch.items():
    out = out + i + str(count)
print(out)'''
# write python program input=a2w2e2f3k4 output=aawweefffkkkk

'''input_st = input("enter a string:")
output=''
for i in input_st:
    if i.isalpha():
        var=i
    else:
        num=int(i)
        output=output+(var*num)
print(output)
'''

# Python program to Count Occurrence of a Character in a String
'''str=input("enetr a string:")
cher=input("enter cheracter:")
cou=0
for i in str:
    if i==cher:
        cou=cou+1
print(cou)'''
# Python Program to Count Total Characters in a String
'''str=input("enetr a string:")
cou=0
for i in str:
    cou=cou+1
print(cou)'''
# Python program to Count Total Number of Words in a String
'''str=input("enter a string:")
st=str.split()
new=len(st)
print(new)'''
# Python program to Count Alphabets Digits and Special Characters in a String
'''str = input("enter a string:")
al = dig = sp = 0
for i in range(len(str)):
    if str[i].isdigit():
        dig=dig+1
    elif str[i].isalpha():
        al=al+1
    else:
        sp=sp+1
print(al)
print("\n",dig)
print("\n", sp)
'''
# fizbuZZ problem
'''def fizzbuzz(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif  i%3==0:
            print('fizz')
        elif i % 5==0:
            print('buzz')
        else:
            print(i)
fizzbuzz(20)'''

# modify the strings
# input=I_am_coder
# output=i.aM.cODER

'''def string_for(s):
    l = []
    temp = s.split('_')
    # print(temp)
    for i in temp:
        l.append(i[0].lower() + i[1:].upper())
    s='.'.join(l)
    print(s)
s="I_am_coder"
string_for(s)'''

'''def string_for(s):
    new=''
    temp=s.split('_')
    for i in temp:
        new=new+i[0].lower() +i[1:].upper() + '.'
    new=new[:-1]
    print(new)
s="I_am_coder"
string_for(s)'''

# armstrong number
'''
n=int(input("enter a number:"))
org=n
sum=0
while n>0:
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if org==sum:
    print("arm")
else:
    print("not")'''

'''
def arm(start, end):
    for i in range(start, end):
        sum = 0
        temp = i
        while temp > 0:
            sum = sum + (temp % 10) * (temp * 10) * (temp * 10)
            temp = temp // 10
        if temp == sum:
            print(temp)


arm(1, 500)'''

# Python example to find Factorial of a Number
n=int(input("enter a number:"))
fac=1
i=1
while n>=i:
    fac=fac*i
    i=i+1
print(fac)

print()
f=1
for i in range(1,n+1):
    f=f*i
print(f)'''
# using recursion
def factorial(n):
    if n==1:
        return 1
    else:
        return (n*factorial(n-1))
n=int(input("enter a number:"))
if n<=0:
    print('no')
else:
    print(factorial(n))


import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return result
    return wrapper

@timing_decorator
# def my_view(request):
