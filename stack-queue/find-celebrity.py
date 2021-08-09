# In a party of N people, only one person is known to everyone. Such a person may be present in the party, if yes, (s)he doesn’t know anyone in the party. We can only ask questions like “does A know B? “. Find the stranger (celebrity) in the minimum number of questions.
# We can describe the problem input as an array of numbers/characters representing persons in the party. We also have a hypothetical function HaveAcquaintance(A, B) which returns true if A knows B, false otherwise.

# Input:
# MATRIX = [ [0, 0, 1, 0],
#            [0, 0, 1, 0],
#            [0, 0, 0, 0],

#            [0, 0, 1, 0] ]
# Output:id = 2
# Explanation: The person with ID 2 does not 
# know anyone but everyone knows him

# Input:
# MATRIX = [ [0, 0, 1, 0],
#            [0, 0, 1, 0],
#            [0, 1, 0, 0],
#            [0, 0, 1, 0] ]
# Output: No celebrity

def check(mat):
    n = len(mat) 
    # for i in range(len(mat)):
    #     if not any(mat[i]):
    #         return i
    # return 'No celebrity'

    stack = [i for i in range(len(mat))]
    while len(stack)>1:
        a = stack.pop()
        b = stack.pop()
        if mat[a][b] == 1:
            stack.append(b)
        else:
            stack.append(a)
        # print(stack)
    if len(stack)<0:
        return 'No celebrity'
    c = stack.pop()
    # print(c)
    for i in range(len(mat)):
        if i!=c and (mat[i][c] == 0 or mat[c][i]==1):
            return 'No celebrity'
    return c
    
if __name__ == "__main__":
    mat = [ [0, 0, 1, 0],[0, 0, 1, 0],[0, 0, 0, 0],[0, 0, 1, 0] ]
    print(check(mat))


# # 0 1 2 3 
# 0 1 2
# 0 2
# 2





