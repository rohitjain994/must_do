def solveNQueens(n):
    	sols = []
	def dfs(state, pd, nd):
		r = len(state)
		if r < n:
			for c in range(n):
				if c not in state and c-r not in pd and c+r not in nd:
					dfs(state+[c], pd|{c-r}, nd|{c+r})
		else: 
			sols.append(state)
	
	dfs([], set(), set())
	return [[f"{'.'*p}Q{'.'*(n-p-1)}" for p in sol] for sol in sols]

# The rules here are for any two queues, they can't share 1)same row, 2)same column, 3)same positive-slope diagonal (col.idx-row.idx), and 4)same negative-slope diagonal (col.idx+row.idx).

# We can use an array to express a game state. Each index indicate queue's row and each value indicate queue's column.
# e.g. [1,3,0,2] expressed a game state as:

# ".Q.."
# "...Q"
# "Q..."
# "..Q."
# So there is only one value in each index ensures rule #1. All values are unique ensures rule #2. I used another two sets pd and nd to store all visited (c-r) and (c+r) to ensures rules #3 and #4. During DFS, in each iteration, we add new column values to our current row array. Rule #1 is already fulfilled as we only add one column value in current iteration. Then we check rules #2, #3, #4. If the column value pass all three check, we add it as a candidate and keep DFS search.

# If row array's length == n, then we have allocated all queues and the state is one of valid state.