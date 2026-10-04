class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while True:
            while i < len(nums) and nums[i] != val:
                i += 1
            while j > -1 and nums[j] == val:
                j -= 1
            if i < j:
                nums[i],nums[j] = nums[j],nums[i]
            else:
                return i


