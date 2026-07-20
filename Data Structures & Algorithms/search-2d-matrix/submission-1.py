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
    
    def MatrixBinarySearch(self, matrix: List[List[int]], target: int, row_count: int, colum_count: int) -> int:
        if(row_count == 0 or colum_count == 0):
            return False
        
        for i in row_count-1:
            if matrix[i][0] == target:
                return True
            elif matrix[i+1][0] < target:
                continue
            elif matrix[i][0] < target:
                return bsearch(matrix[i], 0, len(matrix[i])-1)
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_count = len(matrix) if matrix else 0
        col_count = len (matrix[0]) if matrix[0] else 0 
        if(len(matrix[0])>0):
            flattened = [num for row in matrix for num in row]
            return self.bsearch(flattened, target, 0, (len(matrix)*len(matrix[0]))-1)
        else:
            return False
        
        