# Soal 1

def crange(a,b):
    return range(a,b+1)

def printnln(a):
    print(a, end="")

def fiib(a):
    if a <= 2:
        return 1
    else:
        return fib(a-1) + fib(a-2)

# 1,1,2,3,5,8....

def fib(a):
    if a <= 2:
        return 1
    else:
        return fib(a - 1) + fib(a - 2)
    
for n in crange(1,9):    
    print(fib(n))

print()    


# Soal2

def fib3(a):
    if a <= 3:
        return 1
    else:
        return fib3(a - 1) + fib3(a - 2) + fib3(a - 3)
for n in crange(1,9):
    print(fib3(n)) 

print()       


# Soal 3

def fpb(a,b):
    if b == 0:
        return a
    else:
        return fpb(b, a % b)

printnln("FPB 15 dan 24 adalah ")
print(fpb(15,24))

def kpk(a,b):
    return a * b // fpb(a ,b)

printnln("KPK dari 15 dan 24 adalah ")
print(kpk(15,24))

print()

# Soal 4

for y in crange(1,9):
    for x in crange(1,9):
        if x == y:
            j = y * 2 - 1
            printnln(j)
        elif x == 9 - (y - 1):    
            n = x * 2 - 2
            printnln(n)
        elif x > y and x < 9 - (y - 1):
            printnln("A")
        elif x < y and x > 9 - (y - 1):
            printnln("C")
        elif x < y and x < 9 - (y - 1):
            printnln("D")
        elif x > y and x > 9 - (y - 1):
            printnln("B")
        else:
            printnln("_")
    print() 

print()    

# Soal 5

a = 5
for n in crange(-a, a):
    r = a - abs(n) 
    print(r + 1)

print()                         
    
# 1, 2, 3, 4, 5, 4, 3, 2, 1 = 9
bound = 9 // 2

for n in crange(-bound, bound):
    abad = abs(n)
    res = bound - abad
    print(res)

print()    


# x
for y in crange(-4, 4):
    for x in crange(-4, 4):
        a = abs(x)
        printnln(a)
    print()    

print()
# y

for y in crange(-4, 4):
    for x in crange(-4, 4):
        a = abs(y)
        printnln(a)
    print()
    
print()    

# next

# r = ax > ay ? ax : ay (ternary operator)
# if else

#variabelx =  A > B ? 2: 1 # ?: java, c#, swift, javascript

# if 2 > 1:
#    return 2
# else:
#   return 1

variablex = 2 if "A" == "a" else 1
print(variablex)

print()
for y in crange(-4, 4):
    for x in crange(-4, 4):
        ax = abs(x)
        ay = abs(y)
        r = ax if ax > ay else ay
        r = 4 - r + 1 
        printnln(r)
    print()    

print()

# soal 6
for y in crange(-4, 4):
    for x in crange(-4, 4):
        n = abs(x) if abs(x) > abs(y) else abs(y)
        n = 4 - n + 1
        if n == 5:
            printnln(5)
        elif n == 4:
            printnln(" ")
        elif n == 3:
            printnln(3)
        elif n == 2:
            printnln(" ")            
        else:
            printnln(1)  
    print()

print()

# Soal 7

for y in crange(-4, 4):
    for x in crange(-4, 4):
        n = abs(x) if abs(x) > abs(y) else abs(y)
        n = 4 - n + 1
        if n == 5:
            printnln(2)
        elif n == 4:
            printnln(" ")
        elif n == 1:
            printnln(1)
        elif n == 2:
            printnln(" ")            
        else:
            printnln(1)  
    print()

print()

# Soal 8
for y in crange(-4, 4):
    for x in crange(-4, 4):
        n = abs(x) if abs(x) > abs(y) else abs(y)
        n = 4 - n + 1
        if n == 5:
            printnln(2)
        elif n == 4:
            printnln("B")
        elif n == 1:
            printnln(1)
        elif n == 2:
            printnln("A")            
        else:
            printnln(1)  
    print()
