from collections import defaultdict

class Solution:
    def getHash(self, word: str) -> str:
        hash = [0] * 26
        for c in word:
            hash[ord(c) - ord('a')] += 1

        return tuple(hash)   

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        
        for word in strs:
            map[self.getHash(word)].append(word)
        
        return list(map.values())
