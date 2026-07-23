
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0

        while l<=r:
            mid = (l+r)//2

            hour = 0
            for pile in piles:
                hour += math.ceil(pile/mid)

            if hour <= h:
                r = mid-1
                res = mid
            elif hour >= h:
                l = mid+1
        return res        





        