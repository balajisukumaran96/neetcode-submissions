class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getHashKey(word: str) -> str:
            char_count = [0] * 26
            
            for letter in word:
                char_count[ord(letter)-ord('a')] += 1

            return ','.join(map(str,char_count))

        result = dict()

        for word in strs:
            hash_key = getHashKey(word)

            anagrams = result.get(hash_key, [])
            anagrams.append(word)

            result[hash_key] = anagrams

        return list(result.values())
            