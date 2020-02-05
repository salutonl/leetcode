class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        j = 0
        if length < 2:
            return length
        for i in range(1, length):
            if nums[i] > nums[j]:
                j = j + 1
                nums[j] = nums[i]
        return j + 1