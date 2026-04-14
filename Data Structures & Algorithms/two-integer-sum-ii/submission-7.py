class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) -1 

        while l < r:
            lr = numbers[r] + numbers[l]
            
        
            if lr > target:
                r=r-1

            elif lr < target:
                l =l+1
        
            else:
                return [l+1,r+1]
        return []