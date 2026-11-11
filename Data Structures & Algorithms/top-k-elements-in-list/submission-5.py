class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums)+1)]
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
        
        for key, value in list(hashmap.items()):
            count[value].append(key)

        res = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res

