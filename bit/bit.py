def toggleBitsFromLToR(n,l,r):
     
    # calculating a number
    # 'num' having 'r'
    # number of bits and
    # bits in the range l
    # to r are the only set bits
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1)
  
    # toggle bits in the
    # range l to r in 'n'
    # Besides this, we can calculate num as: num=(1<<r)-l .
 
    # and return the number
    return (n ^ num)
 
# Driver code
 
n = 50
l = 2
r = 5

print(toggleBitsFromLToR(n, l, r))

def swapBits(x) :
     
    # Get all even bits of x
    even_bits = x & 0xAAAAAAAA
 
    # Get all odd bits of x
    odd_bits = x & 0x55555555
     
    # Right shift even bits
    even_bits >>= 1
     
    # Left shift odd bits
    odd_bits <<= 1
 
    # Combine even and odd bits
    return (even_bits | odd_bits)
 
 
# Driver program
# 00010111
x = 23
 
# Output is 43 (00101011)
print(swapBits(x))