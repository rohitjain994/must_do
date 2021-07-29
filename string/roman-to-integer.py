class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I': 1, 'V': 5, 'X': 10 , 'L': 50 , 'C': 100 , 'D': 500 , 'M': 1000}
        prev = 0
        total = 0
        for c in s:
            i = m[c]
            if prev < i :
                total += i - 2*prev
            else: 
                total += i
            prev = i
        return total
            