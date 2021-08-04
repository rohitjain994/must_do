# Function to reverse bits of a given integer
def reverseBits(n):
 
    pos = SIZE - 1      # maintains shift
 
    # store reversed bits of `n`. Initially, all bits are set to 0
    reverse = 0
 
    # do till all bits are processed
    while pos >= 0 and n:
 
        # if the current bit is 1, then set the corresponding bit in the result
        if n & 1:
            reverse = reverse | (1 << pos)
 
        n >>= 1         # drop current bit (divide by 2)
        pos = pos - 1   # decrement shift by 1
 
    return reverse
 
 
if __name__ == '__main__':
 
    n = -100
    SIZE = 32
 
    print(n, "in binary is" + bin(n))
    print("On reversing bits", bin(reverseBits(n)))