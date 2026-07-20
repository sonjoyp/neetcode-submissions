class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_value = nums[0]
        left, right = 0, len(nums)-1
        while (left <= right):
            if(nums[left]<=nums[right]):
                min_value = min(min_value, nums[left])
                break
            
            mid = (left + right) //2
            min_value = min(min_value, nums[mid])

            if(nums[mid]>= nums[left]):
                left = mid + 1
            else:
                right = mid - 1

        return min_value