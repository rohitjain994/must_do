class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(s,p):
            i = 0
            for c in s:
                if i<len(p) and c == p[i]:
                    i+=1
                elif c<'a':
                    return False
            return len(p)==i
        res = []
        for q in queries:
            res.append(match(q,pattern))
        return res
