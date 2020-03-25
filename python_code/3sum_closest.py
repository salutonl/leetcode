class Solution:
    def threeSumClosest(self, nums, target):
        sort_list = sorted(nums)
        if len(sort_list) <= 3:
            return sum(sort_list)
        res = sum(sort_list[:3])
        for i in range(len(sort_list) - 2):
            j, k = i + 1, len(sort_list) - 1
            while j < k:

                total = sort_list[i] + sort_list[j] + sort_list[k]
                if total == target:
                    return total
                if abs(target - total) < abs(target - res):
                    res = total

                if total > target:
                    k -=  1
                else:
                    j += 1
        return res