class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1

        if 2 <= len(numbers) <= 100 and -1000 <= target <= 1000 and -1000 <= numbers[l] <= 1000 and -1000 <= numbers[r] <= 1000:
            while l<r:
                curSum = numbers[l] + numbers[r]
                if curSum < target:
                    l +=1
                elif curSum > target:
                    r -=1
                else:
                    return [l+1,r+1]

