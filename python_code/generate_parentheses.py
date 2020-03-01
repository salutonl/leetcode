class Solution:
    def generateParenthesis(self, n: int):
        def recursion(open_p, close_p, case, res):
            if open_p == 0 and close_p == 0:
                res.append(case)
                return res
            if open_p > 0:
                recursion(open_p - 1, close_p, case + '(', res)
            if close_p > open_p:
                recursion(open_p, close_p - 1, case + ')', res)
            return res

        res = recursion(n, n, '', [])
        return res