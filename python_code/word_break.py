class Solution:
    def wordBreak(self, s, wordDict):
        start = 0
        while s:
            for wb in wordDict:
                length = len(wb)
                if wb == s[start: start + length]:
                    start += length
                    s = s[start - 1:]
                    break
        return True if not s else False
