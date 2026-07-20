class Solution:
    def bsearch(self, nums: List[int], target: int, low: int, high: int) -> int:
        if(low>high):
            return False
        mid = (low + high)//2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            return self.bsearch(nums, target, mid+1, high)
        else:
            return self.bsearch(nums, target, low, mid-1)
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if(len(matrix[0])>0):
            flattened = [num for row in matrix for num in row]
            return self.bsearch(flattened, target, 0, (len(matrix)*len(matrix[0]))-1)
        else:
            return False
        
        