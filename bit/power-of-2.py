import math
def nextroundup(n):
    while n&(n-1):
        n = n&(n-1)
    return n<<1
def prvroundup(n):
    while n&(n-1):
        n = n&(n-1)
    return n
def ispowerof2(n):
    return n>0 and n&(n-1) == 0
def ispowerof4(n):
    return n>0 and n&(n-1) == 0 and n%3 == 1
def ispowerof4b(n):
    return n>0 and n&(n-1) == 0 and n&(0xAAAAAAAA)==0
def ispowerof4a(n):
    i = math.log(n)/math.log(4)
    return i == math.floor(i)

def ispowerof8(n):
    return n>0 and n&(n-1) == 0 and (n & 0xB6DB6DB6) ==0
print(nextroundup(127))
print(prvroundup(127))
print(ispowerof2(128))
