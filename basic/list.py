l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [8, 7, 6, 5, 4, 3, 2]
# Python Program to Append an Item to a List
'''l1.append(8)
print(l1)
l1.insert(2,3)
print(l1)'''
# Python example to access List Index and Values
'''print("list index and value:")
for i in range(len(l1)):
    print("index number:", i, "and value=", l1[i])

l3=([list((i,l2[i])) for i in range(len(l2))])
print(l3)

l4=([(i,l2[i]) for i in range(len(l2))])
print(l4)'''
# Python example to add two Lists
'''print(l1+l2)
l3=l1+l2
print(l3)'''
# Python example to check List is Empty or Not
'''l=[]
if not l:
    print("empity")
else:
    print("not")

if len(l)==0:
    print("empty")
else:
    print("not")'''
# Python Program to Calculate the Average of List Items
'''sum=sum(l1)
print(sum)
avg= sum / len(l1)
print(avg)'''
'''avglist=[]
nu=int(input("Enetr a number of list item:"))
for i in range(1, nu+1):
    valu=int(input("Enetr a number of specific %d subject:" %i))
    avglist.append(valu)
total=sum(avglist)
avg=total/nu
print("\n sum of list:", total)
print("\n average of list:", avg)'''

# Python program to Count Even and Odd Numbers in a List
'''odd, evn= 0,0
for i in l1:
    if i % 2 == 0:
        evn=evn+1
    else:
        odd=odd+1
print("even number:", evn)
print("odd number:", odd)'''
'''evn,odd=0,0
li=[]
nu=int(input("enter a number:"))
for i in range(1,nu+1):
    valu=int(input("enter a number %d:" %i))
    li.append(valu)
for j in range(nu):
    if li[j] % 2==0:
        evn=evn+1
    else:
        odd=odd+1
print("\n totla number of even:", evn)
print("\n totla number of odd:", odd)
'''

# Python example to Clone or Copy a List
'''# using slicing
new=l1[:]
print(new)
# using list function
ne=list(l1)
print(ne)
# using copy function
newlist=l1.copy()
print(newlist)'''

# Python program to Count Positive and Negative Numbers in a List
'''po, neg = 0, 0
for i in l1:
    if i >= 0:
        po = po + 1
    else:
        neg = neg + 1

print("\n + number:", po)
print("\n - number:", neg)


nu=int(input("enter a number range:"))
l=[]
p,n=0,0
for i in range(1, nu+1):
    valu=int(input("enetr a number %d :" %i))
    l.append(valu)

for j in range(nu):
    if l[j] >=0:
        p=p+1
    else:
        n=n+1
print("\n total + number:", p)
print("\n total - number:", n)'''
# Python program to Print Largest and Smallest Number
'''print(max(l1))
print(min(l1))'''
# Python program to find Length of a List
# print(len(l1))
# Python program to find List Difference
'''diff1=list(set(l1)-set(l2))
diff2=list(set(l2)-set(l1))
actdiff= diff1+diff2
print(actdiff)'''
# Python List Multiplication Program
'''nu=int(input("Enter a range of list:"))
L=[]
for i in range(1, nu+1):
    valu=int(input("Enter a number in list %d :"%i))
    L.append(valu)
print("orignal list:",L)

mul=1
for i in range(nu):
    mul=mul*L[i]
print("multiplication of list:", mul)'''

# Python Program to Print List Items in Reverse Order
'''l1.reverse()
print(l1)

print(l1[::-1])

l1.reverse()
print(l1)

for i in range(len(l2) - 1, -1, -1):
    print(l2[i], end=' ')

lis = []
nu = int(input("Enter a number:"))
for i in range(0, nu+1):
    val=int(input("Enetr a number %d :" %i))
    lis.append(val)
print("Original list:", lis)
for i in range(len(lis) -1,-1,-1):
    print("after rev", lis[i],end=' ')
'''


# Python Program to find Largest Number in a List

'''max = l1[0]

for i in l1:
    if i > max:
        max = i

print("Largest element in the list is:", max)'''

# Python Program to Print List Items at Even Position
'''list=[1,2,3,4,5,6,7]
for i in range(1,len(list),2):
    print(list[i], end=' ')
# using while loop
i=1
while i < len(list):
    print(list[i], end=' ')
    i=i+2'''
# Python Program to Print List Items at Odd Position

'''for i in range(0, len(l1),2):
    print(l1[i], end=' ')
print("\n")
L=[14, 35, 78, 90, 120, 67, 98]
i=0
while i<len(l2):
    print(l2[i],end=' ')
    i=i+2
'''