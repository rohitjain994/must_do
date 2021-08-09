# Python program to count
# all distinct binary strings
# without two consecutive 1's
 
def countStrings(n):
 
    a=[0 for i in range(n)]
    b=[0 for i in range(n)]
    a[0] = b[0] = 1
    for i in range(1,n):
        a[i] = a[i-1] + b[i-1]
        b[i] = a[i-1]
     
    return a[n-1] + b[n-1]
 
# Driver program to test
# above functions
 
print(countStrings(3))
 
# This code is contributed
# by Anant Agarwal.

# If we take a closer look at the pattern, we can observe that the count is actually (n+2)’th Fibonacci number for n >= 1. The Fibonacci Numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 141, …. 

# n = 1, count = 2  = fib(3)
# n = 2, count = 3  = fib(4)
# n = 3, count = 5  = fib(5)
# n = 4, count = 8  = fib(6)
# n = 5, count = 13 = fib(7)
# ................
# Therefore we can count the strings in O(Log n) time also using the method 5 