from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_frequent = Counter(nums).most_common()
        return [value for value, count in most_frequent[:k]]    