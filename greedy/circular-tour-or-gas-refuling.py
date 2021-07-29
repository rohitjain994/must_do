class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        s,e = len(gas)-1,0
        bal = gas[s]-cost[s]
        while s>e:
            if bal>=0:
                bal+=gas[e]-cost[e]
                e+=1
            else:
                s-=1
                bal+=gas[s]-cost[s]
        return s if bal>=0 else -1