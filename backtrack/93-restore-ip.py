class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s,0,"",res)
        return res
    def dfs(self,s,idx,path,res):
        if idx ==4:
            if not s:
                res.append(path[:-1])
            return
        for i in range(1,4):
            if i<=len(s):
                if s[:i]=='0' or ( s[0]!='0' and 0<int(s[:i])<256):
                    self.dfs(s[i:],idx+1,path+s[:i]+'.',res)

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]