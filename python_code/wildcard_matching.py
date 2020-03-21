class Solution:
    def isMatch(self, s, p):
        dp = [[True] + [False] * len(s)]
        for i in range(len(p)):
            dp.append([False] * (len(s) + 1))
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                dp[i][0] = dp[i - 1][0]
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] in {s[j - 1], '?'}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        return dp[-1][-1]
