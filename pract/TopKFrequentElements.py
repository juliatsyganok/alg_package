from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        s = sorted(d.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in s[:k]]
