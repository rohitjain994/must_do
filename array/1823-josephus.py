class Solution:
    # def findTheWinner(self, n: int, k: int) -> int:
    #     if n==1:
    #         return 1
    #     return (self.findTheWinner(n-1,k)+k-1)%n + 1
    
# O(n)    
    def findTheWinner(self, n, k):
        n = list(range(1,n+1))
        return self.josephus(n, k)
        
    def josephus(self, ls, skip):
        skip -= 1 
        idx = skip
        while len(ls) > 1:
            ls.pop(idx)
            idx = (idx + skip) % len(ls)
        return ls[0]
    #famous Josephus problem O(n^2)
    