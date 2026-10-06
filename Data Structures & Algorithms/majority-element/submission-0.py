class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bit_counter = [0] * 31
        result = 0
        sign = 0
        for num in nums:
            sign = sign + 1 if num > 0 else sign - 1
            for i in range(31):
                if (abs(num) >> i) & 1:
                    bit_counter[i] += 1
        for i, cnt in enumerate(bit_counter):
            # print(i, " ", cnt)
            if cnt > (len(nums) // 2):
                # print(i, " x ", cnt)
                result += 2**i
        result = -result if sign < 0 else result
        return result
