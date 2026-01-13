num=int(input("enter a number"))
if num==0:
    print("zero")
elif num>=0:
    print("pos")
else:
    print("neg")


    
     
num=int(input("enter a number"))
if num % 2==0:
    print("even")
else:
    print("odd") 


a=10
b=20
c=30
if a>b:
    if a>c:
        print("a")
    else:
        print("c")
elif b>c:
    print("b")
else:
    print("c")

    

year=int(input("enter year"))
if year%4==0:
    print("leaf year")
else:
    print("not leaf year")




marks=int(input("enter marks"))   
if marks >=90:
    print("A")
elif marks >=75:
    print("B")
elif marks>=50:
    print("c")
else:
    print("fail")



a=10
b=20
c=30
if a>b:
    if a>c:
        print("a")
    else:
        print("c")
elif b>c:
    print("b")
else:
    print("c")    


num=10
for i in range (0,num):
    print(i)



num=10
for i in range(0,num):
    c=i*2
    print(c)


n=int(input("enter a number"))
s=0
for i in range(1,n+1):
    s=s+i
print(s)


n+ int(input("enter = "))
c=0
while n>0:
    c=c+1
    n=n//10
print(c) 
n=int(input("enter"))
rev=0
while n!=0:
    rev=rev*10+n%10
    n//=10
print(rev)    


for i in range(2,101,2):
    print(i)



n = int(input())
f = 0

for i in range(2, n):
    if n % i == 0:
        f = 1

if f == 0:
    print("Prime")
else:
    print("Not Prime")
    
n = int(input())
a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
n = int(input())
s = 0

while n > 0:
    s = s + n % 10
    n = n // 10

print(s)
def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f
def big(a, b, c):
    return max(a, b, c)
def si(p, r, t):
    return (p*r*t)/100
def pal(n):
    return str(n) == str(n)[::-1]
def primes(a, b):
    for n in range(a, b+1):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                print(n)
def count(s):
    v = 0
    c = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            v += 1
        else:
            c += 1
    print(v, c)
def arm(n):
    s = 0
    t = n
    while t > 0:
        d = t % 10
        s = s + d*d*d
        t = t // 10
    return s == n
def fib(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        a, b = b, a+b
def even_odd(lst):
    e = 0
    o = 0
    for n in lst:
        if n % 2 == 0:
            e += n
        else:
            o += n
    print(e, o)
