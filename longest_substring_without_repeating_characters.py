class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxNum = 0
        tempString = ""

        for character in s:
            if character not in tempString:
                tempString += character
            else:
                maxNum = max(maxNum, len(tempString))
                tempString = tempString[tempString.index(
                    character) + 1:] + character
        return max(maxNum, len(tempString))
