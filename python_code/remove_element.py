class Solution:
    def removeElement(self, nums, val):
        """
        :param nums:
        :param val:
        :return:
        """
        index = 0
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] == val:
                start += 1
            elif nums[end] == val:
                end -= 1
            else:
                nums[index] = nums[start]
                index += 1
                start += 1
        return index