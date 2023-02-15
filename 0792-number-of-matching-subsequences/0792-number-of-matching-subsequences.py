from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        wordict = defaultdict(list)
        count=0
        for word in words:
            wordict[word[0]].append(word)
        for char in s:
            expect = wordict[char]
            
            wordict[char]=[]
        
            for word in expect:
                if len(word)==1:
                    count+=1
                else:
                    wordict[word[1]].append(word[1:])
        return count
        