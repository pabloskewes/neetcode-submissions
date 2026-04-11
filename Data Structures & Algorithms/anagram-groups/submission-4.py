from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters = defaultdict(list)

        for string in strs:
            counter = tuple(sorted(string))
            counters[counter].append(string)
        
        return [v for _, v in counters.items()]