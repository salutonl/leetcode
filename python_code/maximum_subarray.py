class Solution:
    def maxSubArray(self, nums):
        res = cur_sum = nums[0]
        for i in nums[1:]:
            cur_sum = max(i, cur_sum + i)
            res = max(res, cur_sum)
        return res



