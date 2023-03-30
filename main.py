# def change(s):
#     f,*mi,l=s.split()
#     print(l,*mi,f)
# s=input("enter a string:")


# input=aawwwkk outpu=a2w3k2

# stri=str(input("enter a string:"))
# dic={}
# for i in stri:
#     if i in dic:
#         dic[i]=dic[i]+1
#     else:
#         dic[i]=1
# print(dic)
# out=''
# for i,cou in dic.items():
#     out=out+i+str(cou)
# print(out)
# out=''
# for i in stri:
#     if i.isalpha():
#         var=i
#     else:
#         tem=int(i)
#         out=out+(var*tem)
# print(out)

# def st(s):
#     lis=[]
#     temp=s.split('_')
#     print(temp)
#     for i in temp:
#         lis.append(i[0].lower()+i[1:].upper())
#     s='.'.join(lis)
#     print(s)
# s='i_am_coder'
# st(s)

# def stri(s):
#     new=''
#     temp=s.split('_')
#     print(temp)
#     for i in temp:
#         new=new+i[0].lower()+i[1:].upper()+'.'
#     new=new[:-1]
#     print(new)
# s='s_ssssjk_kkiu'
# stri(s)
#
# stri=str(input("enetr:"))
# ch=str(input("enetr a cher"))
# cou=0
# for i in stri:
#     if i==ch:
#         cou=cou+1
# print(cou)
# stri=str(input("enetr:"))
# cou=''
# for i in stri:
#     if i>='A' and i<='Z':
#         cou=cou+chr(ord(i)+32)
#     else:
#         cou=cou+1
#
# print(cou)
# st=input("enetr a string:")
# dic={}
# for i in st:
#     if i in dic:
#         dic[i]=dic[i]+1
#     else:
#         dic[i]=1
# print(dic)
# out=''
# for i,count in dic.items():
#     out=out+i+str(count)
# print(out)
# st=str(input("enetr a string:"))
# new=''
# for i in st:
#     if i.isalpha():
#         var=i
#     else:
#         temp=int(i)
#         new=new+(var*temp)
# print(new)

# def pal(n):
#     f=0
#     l=n-1
#     while f<l:
#         if n[f]==n[l]:
#             f=f+1
#             l=l-1
#         else:
#             print("nort")
#     print("palindrom")
# n=input("emnetr")
# pal(n)

# st=str(input("enetr a string:"))
# n=len(st)
# for i in range(n):
#     if st[i]!=st[n-i-1]:
#         print("not")
# print("ppp")

# list=[1,1,1,2,2,3,3,4,4,5,6]
# new=[]
# for i in list:
#     if list.count(i)==1:
#         new.append(i)
# print(new)
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i]==list[j] and list[i] not in new:
#             new.append(list[i])
# print(new)
#
# n=int(input("enter a number:"))
# num=n
# sum=0
# while num>0:
#     tem=(num%10)*(num%10)*(num%10)
#     sum=sum+tem
#     num=num//10
# if n==sum:
#     print("ppp")
# else:
#     print("not")
# print(sum)
# l=int(input("enetr 1 :"))
# f=int(input("enetr u :"))
# for num in range(l,f+1):
#     sum=0
#     n=num
#     while n>0:
#         tem=(n%10)*(n%10)*(n%10)
#         sum=sum+tem
#         n=n//10
#         if num==sum:
#             print(num)
# print()
#
# lower = int(input("Enter lower range: "))
# upper = int(input("Enter upper range: "))
#
# for num in range(lower, upper + 1):
#     sum = 0
#     n = num
#     while n > 0:
#         digit =(n%10)*(n%10)*(n%10)
#         sum=sum+digit
#         n=n// 10
#         if num == sum:
#             print(num)
import re

# Define a string
my_string = "The quick brown fox jumps over the lazy dog."

# Search for a pattern within the string
pattern = "fox"
match = re.search(pattern, my_string)
print(match)

# Print the result
if match:
    print("Found match:", match.group(0))
else:
    print("No match found.")