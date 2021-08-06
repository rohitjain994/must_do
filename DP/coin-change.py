# Function to find the total number of distinct ways to get
# a change of `N` from an unlimited supply of coins in set `S`
def count(S, N):
 
    T = [0] * (N + 1)
    T[0] = 1
 
    for i in range(len(S)):
        for j in range(S[i],N+1):
            T[j] += T[j - S[i]]
    return T[N]
 
 
if __name__ == '__main__':
 
    # `n` coins of given denominations
    S = 1, 2, 3
 
    # total change required
    N = 4
 
    print("The total number of ways to get the desired change is", count(S, N))