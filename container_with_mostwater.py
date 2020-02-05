class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        start = 0
        end = len(height) - 1
        while start < end:
            area = (end - start) * min(height[start], height[end])
            res = area if area > res else res
            lp = start
            rp = end
            if height[start] <= height[end]:
                lp += 1
                while lp < rp and height[lp] <= height[start]:
                    lp += 1
            if height[end] <= height[start]:
                rp -= 1
                while rp > lp and height[rp] <= height[end]:
                    rp -= 1
            start = lp
            end = rp

        return res
            

