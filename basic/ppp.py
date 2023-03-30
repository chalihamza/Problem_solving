'''def fun(lis):
    lis.sort()
    print(lis[1])
    print(lis[-2])
lis=[2,3,4,5,5,6]
fun(lis)'''

'''def fun(s):
    f,*m,l=s.split()
    print(l,*m,f)
s="ali hamza riaz usama"
fun(s)'''

# s=dict(sorted(d.items(), key=lambda x:x[1][1]))
'''
def pa(s):
    tem=s[::-1]
    if s==tem:
        print("ppp")
    else:
        print("not")
s="ala"
pa(s)'''

'''def pil(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n - i - 1]:
            return False
    print('pil')


s = 'ala'
pil(s)'''

'''n = int(input("enter a number:"))
tem = n
re = 0
while tem > 0:
    rem = tem % 10
    re = (re * 10) + rem
    tem = tem // 10
if n == re:
    print('pp')
else:
    print('no')

new=int(str(n)[::-1])
print(new)'''

'''def fib(n):
    f=0
    s=1
    print(f)
    while n>s:
        print(s)
        f,s=s, f+s
fib(50)'''

'''
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

n = 50
if n <= 0:
    print("invalid input")
else:
    for i in range(n):
     print(fib(i))'''

'''
s=input("enter a string:")
ch={}
for i in s:
    if i in ch:
        ch[i]=ch[i]+1
    else:
        ch[i]=1
print(ch)
out=''
for i,count in ch.items():
    out=out+i+str(count)
print(out)'''

'''s=input("enter a string:")
out=''
for i in s:
    if i.isalpha():
        new=i
    else:
        var=int(i)
        out=out+(var*i)
print(out)'''

'''
def st(s):
    n = []
    tem = s.split('_')
    print(tem)
    for i in tem:
        n.append(i[0].lower() + i[1:].upper())
    s = '.'.join(n)
    print(s)


s = 'ali_hamza'
st(s)


def stri(s):
    l = ''
    tem = s.split('_')
    print(tem)
    for i in tem:
        l = l + i[0].lower() + i[1:].upper() + '.'
    l = l[:-1]
    print(l)


s = "ali_hamza_riaz"
stri(s)'''

'''n=int(input("enetr a number:"))
sum=0
new=n
while n>0:
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if new==sum:
    print("arm")
else:
    print("not")'''

'''n = int(input("enter a number:"))
fac = 1
i = 1
while n >= i:
    fac = fac * i
    i = i + 1
print(fac)'''


def decurater_fun(fun):
    def wraper_fun():
        print("wraper_fun")
        return fun()

    print("decurater_fun")
    return wraper_fun()


@decurater_fun
def display():
    print("display fun")



