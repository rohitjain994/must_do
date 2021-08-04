class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dmap = {}
        idx,_max = 0,0
        for i in range(len(s)):
            if s[i] in dmap and idx <= dmap[s[i]]:
                idx = dmap[s[i]]+1
            else:
                _max = max(_max,i-idx+1)
            dmap[s[i]]=i
        return _max