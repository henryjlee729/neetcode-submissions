class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            countArray = [0] * 26
            for c in word:
                if 'a' <= c <= 'z':
                    countArray[ord(c) - ord('a')] += 1
            
            countArray = tuple(countArray)
            if countArray in hashmap.keys():
                hashmap[countArray].append(word)
            else:
                hashmap[countArray] = [word]

        return list(hashmap.values())