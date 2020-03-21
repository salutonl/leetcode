class Solution:
    def searchInsert(self, nums, target):
        position = 0
        length = len(nums)
        if target < nums[0]:
            return 0
        elif target > nums[length - 1]:
            return length
        elif target == nums[length - 1]:
            return length - 1
        else:
            for i in range(length - 1):
                if nums[i] == target:
                    return i
                if target > nums[i] and target < nums[i + 1]:
                    position = i + 1
        return position