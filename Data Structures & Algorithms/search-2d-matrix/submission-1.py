class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                l, r = 0, len(row)-1
                while l<=r:
                    mid = (l+r)//2
                    if row[mid] < target:
                        l+=1
                    elif row[mid] > target:
                        r -=1
                    elif row[mid] == target:
                        return True
        return False                        