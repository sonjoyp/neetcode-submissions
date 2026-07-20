class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_value = nums[0]
        left, right = 0, len(nums)-1
        while (left <= right):

            # corner case 1
            if(nums[left]<=nums[right]):
                min_value = min(min_value, nums[left])
                break
            
            # corner case 2
            mid = (left + right) //2
            min_value = min(min_value, nums[mid])
            
            # search direction
            if(nums[mid]>= nums[left]):
                left = mid + 1
            else:
                right = mid - 1

        return min_value