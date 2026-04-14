class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = False
        for i in matrix:
            for j in i:
                if j ==target:
                    res = True
                    break
        return res