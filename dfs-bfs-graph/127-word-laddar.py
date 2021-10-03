from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            # print("word not exist")
            return 0
        que = [beginWord]
        depth = 0
        while que :
            depth += 1
            lsize = len(que)
            while lsize:
                curr = que.pop(0)
                for i in range(len(curr)):
                    for c in range(ord('a'),ord('z')+1):
                        temp = curr[:i] + chr(c) + curr[i+1:]
                        # print(temp)
                        if temp in wordset:
                            que.append(temp)
                            wordset.remove(temp)
                        if temp == endWord:
                            return depth+1
                lsize -=1
        print(depth)
        return 0