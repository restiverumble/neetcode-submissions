class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo,hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi)//2
            total_hrs = 0
            for pile in piles:
                total_hrs += math.ceil(pile/mid)
            
            if total_hrs > h:
                lo = mid + 1
            else:
                hi = mid

        return lo
