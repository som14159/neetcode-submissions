class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mappie = {}
        for i in nums:
            if i in mappie:
                return True
            mappie[i] = 1
        return False
        