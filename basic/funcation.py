def add():
    x = 10
    y = 20
    c = x + y
    print(c)


add()


def ad(x, y):
    c = x + y
    print(c)


ad(10, 20)


def ad(y):
    x = 12
    c = x + y
    print(c)


ad(20)


def add(x, y):
    a = x + y
    b = x - y
    return a, b


sum, sub = add(20, 30)
print(sub)
print(sum)


def pow(x, y):
    c = x ** y
    print(c)


pow(2, 4)


def fun(*y):
    z = y[0] + y[1] + y[2]
    print(z)


fun(1, 2, 3)


def fun(x, *y):
    z = x + y[0] + y[1] + y[2] + y[3]
    print(z)


fun(1, 2, 3, 4, 5)


def fun(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print(sum)


fun(2, 3, 4, 5)


def add(**y):
    z = y['a'] + y['b'] + y['c'] + y['d']
    print(z)


add(a=3, b=4, c=5, d=6)


def intro(**data):
    for key, value in data.items():
        print("{} is {}".format(key, value))


intro(Firstname="ali", lastname="hamza", age=24, phone=11111, )

x = lambda a: a + 5
print(x(5))

def fact(x):
    if x==1:
        return 1
    else:
        return (x*fact(x-1))
num=5
print("The factorial of ", num, "is", fact(num))