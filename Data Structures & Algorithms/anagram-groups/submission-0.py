class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmaps = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in hashmaps:
                hashmaps[sorted_s].append(s)
            else:
                hashmaps[sorted_s] = [s]
        return list(hashmaps.values())


