tyu1 = (1, 2, 3, 4, 5, 6,)
tyu2 = ('a', 'b', 'c', 'd', 'e',)
tyu3 = ("mouse", [23, 43, 45], (7, 8, 9, 10))
# tyu3=tyu1+tyu2
# print(id(tyu3))
# print(id(tyu1+tyu2))
# Python Program to Find Tuple Length
'''print("length of a tuple:", len(tyu1))
print("length of a tuple:", len(tyu2))
print("length of a tuple nested:", len(tyu3[0]))'''
# Python example to add an Item to tuple
'''tyu1 = tyu1 + (7, 8, 9, 10,)
print(tyu1)'''
# how to find time
'''import timeit
tyutime=timeit.timeit(stmt="(1,2,3,4,5)")
print(tyutime)'''
# how to find memory space
'''import sys
print("size of tuple:",sys.getsizeof(tyu1))'''
# Python Program to add an Item to tuple
'''nu = int(input("Enter a number:"))
tup = ()
for i in range(1, nu + 1):
    valu = int(input("Enter a %d number:=" % i))
    tup = tup + (valu,)
print("tuple items=", tup)'''
# Python Program to Remove an Item from Tuple
'''tyu1 = (1, 2, 3, 4, 5, 6,)
print(tyu1[:2]+tyu1[4:])'''
'''t=(1,2,3,4,65,94,58,73,6,)
print(t)
new=list(t)
print(new)
new.remove(94)
print(new)
t=tuple(new)
print(t)'''
# Python Program to Slice a Tuple
'''tyu = (1, 2, 3, 4, 5, 6,)
print("tuple:",tyu)
tyu=tyu[3:]
print(tyu)
tyu=tyu[:3]
print(tyu)
tyu=tyu[2:6]
print(tyu)
'''
# Python Program to Check Item exists in Tuple
'''tyu = (1, 2, 3, 4, 5, 6,7,9)
print("orignal tuple:", tyu)
n=int(input("Enter a number="))
if n in tyu:
    print("number is exist:", n)
else:
    print("sorry")'''


