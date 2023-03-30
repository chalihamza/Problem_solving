# class Emp:
#     def __init__(self):
#         self.salary = 2222
#         self.age = 21
#
#
# e1 = Emp()
# print(e1.__dict__)
#

'''def LCM(a,b):
    if a>b:
        grt=a
    else:
        grt=b
    while (True):
        if grt % a == 0 and grt % b ==0:
            lcm=grt
            break
        grt=grt+1
    return lcm
a=int(input("Enetr 1 number"))
b=int(input("Enetr 2 number"))
print("the lcm:", LCM(a,b))
'''

'''def HCF(a,b):
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if smaller % a==0 and smaller % b==0:
            HCF=i
        return HCF'''

'''n=int(input("Enetr a number:"))
cube=n*n*n
# cu=n**3
print(cube)
'''
# n=int(input("enet a number:"))
# new=n
# while new>=10:
#     new=new//10
# print(new)

'''
def remove_duplicates(string):
    result = ''
    for char in string:
        if char not in result:
            result += char
    return result

input_string = 'aaabccdde'
output_string = remove_duplicates(input_string)
print(output_string)'''
'''li=[1,2,3,4,4,4,4]
c=int(input("enter a number"))
count=0
for i in li:
    if i ==c:
        count=count+1
print(count)'''
