class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_found = []
        for num in nums:
            if num not in nums_found:
                nums_found.append(num)
            else:
                return True
        return False