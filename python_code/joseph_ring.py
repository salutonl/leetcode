class Solution:
    def lastRemaining(self, n, m):
        end_pos = 0
        for i in range(2, n + 1):
            end_pos = (end_pos + m) % i
        return end_pos