class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] =True
        for i in range(1,len(s)+1):
            for w in wordDict:
                if dp[i-len(w)] and s[i-len(w):i]==w:
                    dp[i]=True
        return dp[-1]
                
class Solution(object):
    def wordBreak(self, s, wordDict):
        return self.helper(s, wordDict, {})
    
def helper(self, s, wordDict, memo):
    if s in memo: return memo[s]
    if not s: return []
    
    res = []
    for word in wordDict:
        if not s.startswith(word):
            continue
        if len(word) == len(s):
            res.append(word)
        else:
            resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
            for item in resultOfTheRest:
                item = word + ' ' + item
                res.append(item)
    memo[s] = res
    return res