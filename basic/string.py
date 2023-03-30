string = "0123456789"

print(string[5:8])  # 6 not include 15 include
# print(string[:]) #return whole string
# print(string[5])
# print(string[::-1])
'''
str=""
rev_str = ""

#iterate over the string from the last character
for char in "Hello World":
  rev_str = char + rev_str

#print the reversed string
print(rev_str)
'''
# Python Program to Concatenate Strings Example 1
'''a=input("Enetr 1 string:")
b=input("Enter 2 string:")

c=a+b
print(c)'''

# Python Program to Convert String to Uppercase
'''str=input("Enter a string")
s1=str.upper()
print(s1)'''
'''
str=input("Enetr a string:")
result=""
for i in str:
  if i >='a' and i<='z':
    result=result+chr(ord(i)-32)
  else:
    result=result+1

print(str)
print("\n", result)'''

# Python program to Convert String to Lowercase

'''str=input("Enter a string:")
s1=str.lower()
print(s1)'''
'''str=input("Enetr a string:")
re=""
for i in str:
  if i >='A' and i <='Z':
    re=re+chr(ord(i)+32)
  else:
    re=re+i
print(str)
print("\n", re)'''

# Python program to Copy a String
'''str='alihamza'
s1=str[:]
print(str)
print("\n",s1)'''

'''str='ali'
r=""
for i in str:
  r=r+i
print(str)
print(r)'''
# Python program to Count Occurrence of a Character in a String
'''
str = input("Eneter a strong:")
ch = input("Enet a cheracter:")
cou = 0
for i in str:
    if i == ch:
        cou = cou + 1
print(cou)'''

'''def occ(str,ch):
    count=0
    for i in str:
        if i == ch:
            count=count+1
    return count

str = input("Eneter a strong:")
ch = input("Enet a cheracter:")
cnt=occ(str,ch)
print(cnt)'''
# Python Program to Count Characters Frequency in a String
from collections import Counter

'''str = input("Enter a strong:")
char = Counter(str)
print(char)'''

'''str=input("Enetr a string:")
dict={}
for i in str:
    key=dict.keys()
    if i in key:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)'''
# Python Program to Count Total Characters in a String

'''str=input("Enetr a stering:")
l=0
for i in str:
    l=l+1
print(l)'''

# Python program to Count Total Number of Words in a String
'''
str="ali hamza"
new=str.split()
word=len(new)
print(word)'''

'''str='ali hamza riaz'
total=1
for i in range(len(str)):
    if str[i] =='' or str[i]=='\n' or str[i]=='\t':
        total=total+1
print(total)'''
# Python program to Count Vowels in a String

'''str=input("enter a string:")
vo=0
for i in str:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'
            or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vo=vo+1
print(vo)'''

# Python program to Count Vowels and Consonants in a String
'''str=input("Enetr a string:")
vo=0
cou=0
for i in str:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'
            or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vo=vo+1
    else:
        cou=cou+1
print(vo)
print(cou)
'''
# Python program to Count Alphabets Digits and Special Characters in a String
'''str=input("Enter a chera:")
al=dig=spec=0
for i in range(len(str)):
    if str[i].isalpha():
        al=al+1
    elif str[i].isdigit():
        dig=dig+1
    else:
        spec=spec+1
print(al)
print(dig)
print(spec)'''
# Python Program to Check If Two Strings are Anagram

'''st1=input("Enetr 1 st")
st2=input("Enetr 2 st")
if sorted(st1)==sorted(st2):
    print("Two string are argument:")
else:
    print("not")'''
# Python Program to Check a Given String is Palindrome
'''str=input("entera str")
tem=str[::-1]
if tem==str:
    print("Yes")
else:
    print("not")'''

'''def pel(s):
    n=len(s)
    for i in range(n):
        if s[i] != s[n-i-1]:
            return False
        return/ True
s='mam'
print(pel(s))
age=24
dic=24 if age <65 else 10
print(dic)
'''

#
# class Employlee:
#     def __int__(self):
#         self.salary = 2222
#         self.age = 21
import re

# Define a string
my_string = "The quick brown fox jumps over the lazy dog."

# Search for a pattern within the string
pattern = "fox"
match = re.search(pattern, my_string)

# Print the result
if match:
    print("Found match:", match.group(0))
else:
    print("No match found.")

