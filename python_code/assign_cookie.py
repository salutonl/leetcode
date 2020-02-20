class Solution:
    def findContentChildren(self, g, s):
        c_demand = sorted(g)
        cookies = sorted(s)
        c_index = 0
        res = 0
        for cookie in cookies:
            if c_index == len(g):
                return res
            if cookie >= c_demand[c_index]:
                res += 1
                c_index += 1
        return res
