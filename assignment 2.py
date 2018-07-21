# Qn 1
x = int(input("enter the value of x:: "))
m = 0.5
c = 2.5
y = m * x + c
print("the value of y=mx+c is ", y)


# Qn 2

def sum(*args):
    y = len(args)
    sum = 0
    for value in args:
        sum += value
    print("the sum is", sum)


sum(1, 2, 3)

# Qn 3

x = list(range(1, 20))
sum = 0
for value in x:
    sum += value
    if sum > 32:
        break
print("the sum is", sum)

# Qn 4


x = int(input("enter any integer:: "))
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")

# Qn 5


for n in range(2, 50):
    for x in range(2, n):
        if n % x == 0:
            print(n, " is composite")
            break
    else:
        print(n, " is prime")

# Qn 6


x = ["Hello", "my", "name", "is", "John", "Cena"]
y = ' '.join(x)
print(y)


# Qn 7

def hbd(name):
    print("Happy Birthday " + name)


x = input("enter your name:: ")
hbd(x)


# Qn 8

my_number=[1,2,3,4,5,6,7,8,9]
for n in my_number:
    if n%2 != 0:
        print(n**2)


# Qn 10
from collections import namedtuple
from collections import OrderedDict

space_coordinate = namedtuple('coordinate',['x','y','z'])
p = space_coordinate(2,3,4)
print(p)

Roll_no = namedtuple('Roll_no', ['shubham','aabiskar','pradip'])
r = Roll_no(701,702,705)
print(r)

d = OrderedDict(a=120, b=32, c=32320)
print(d)



