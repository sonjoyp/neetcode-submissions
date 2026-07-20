class Solution:
    def bsearch(self, nums: List[int], target: int, low: int, high: int) -> int:
        if(low>high):
            return -1
        mid = (low + high)//2
        print(low, mid, high)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.bsearch(nums, target, mid+1, high)
        else:
            return self.bsearch(nums, target, low, mid-1)

    def search(self, nums: List[int], target: int) -> int:
        print("Lenght=",len(nums)-1)
        return self.bsearch(nums, target, 0, len(nums)-1)