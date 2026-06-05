class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            count_array = [0] * 26
            for c in word:
                if 'a' <= c <= 'z':
                    count_array[ord(c) - ord('a')] += 1
            
            count_array = tuple(count_array)
            if count_array in hashmap.keys():
                hashmap[count_array].append(word)
            else:
                hashmap[count_array] = [word]

        return list(hashmap.values())