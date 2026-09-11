class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index in range(len(nums)):
            diff = target - nums[index]
            num = nums[index]
            if diff in hashmap:
                return [hashmap[diff], index]
            else:
                hashmap[num] = index
