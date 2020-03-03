class Solution:
    def maxSubArray(self, nums):
        le = len(nums)
        array = [[0] * (le + 1) for _ in range(le + 1)]
        res = nums[0]
        for i in range(1, le + 1):
            for j in range(i, le + 1):
                array[i][j] = array[i][j-1] + nums[j - 1]
                print(array[i][j - 1], nums[j - 1])
            res = max(max(array[i][1:]), res)
        print(array)
        print(res)
        return res

res = Solution()
res.maxSubArray([-2, -1])