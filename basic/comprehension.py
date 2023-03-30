# list comprehension
'''a = [i for i in range(20) if i % 2 != 0]
print(a)'''
# l1 = [2, 3, 4]
# l2 = [5, 6, 7]
# l=[]
'''for i in l1:
    for j in l2:
        l.append(i*j)
print(l)

L=[(i*j) for i in l1 for j in l2]
print(L)'''
'''for i in l1:
    for j in l2:
        l.append([i,j])
print(l)

L=[(i,j) for i in l1 for j in l2]
print(L)'''

'''d={}
for i in range(1,10):
    d[i]=i*i
print(d)

D={i:i*i for i in range(1,10) if i % 2==0}
print(D)'''

'''l1 = [i for i in range(3)]
l2 = ['m', 'n', 'o']
dik={}
for (key, value) in zip(l1, l2):
    dik[key] = value
print(dik)

D={key:value for (key, value) in zip(l1,l2)}
print(D)'''
s1={1,2,3,4,5,2,3,4,5}
s2=set()
for i in s1:
    if i %2!=0:
        s2.add(i)
print(s2)

s3={i for i in s1 if i %2!=0}
print(s3)