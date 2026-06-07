from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = Counter(nums).most_common()
        count = 0
        ans = []
        for key, _ in sorted_nums:
            if count == k:
                break
            
            ans.append(key)
            count += 1
    
        return ans