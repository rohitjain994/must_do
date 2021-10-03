# Python3 program to
# Print all combinations
# of balanced parentheses

# Wrapper over _printParenthesis()
def printParenthesis(str, n):
	if(n > 0):
	    _printParenthesis(str, 0,n, 0, 0);
	return

def _printParenthesis(str, pos, n,open, close):
	
	if(close == n):
		print(''.join(str))
		return
	else:
		if(open > close):
			str[pos] = '}'
			_printParenthesis(str, pos + 1, n,open, close + 1)
		if(open < n):
			str[pos] = '{'
			_printParenthesis(str, pos + 1, n,open + 1, close)

# Driver Code
n = 3
str = [""] * 2 * n
printParenthesis(str, n)

# This Code is contributed
# by mits.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def bt(s,l,r):
            if len(s) == 2*n:
                ans.append(''.join(s))
                return 
            if l<n:
                s.append('(')
                bt(s,l+1,r)
                s.pop()
            if r<l:
                s.append(')')
                bt(s,l,r+1)
                s.pop()
        bt([],0,0)
        return ans