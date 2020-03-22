class Solution:
    def lengthOfLastWord(self, s):
        if not s or not s.strip():
            return 0
        words = s.split()
        print(words)
        return len(words[-1])
