class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            palinedrome_list = [int(x) for x in str(x)]
            length = len(palinedrome_list)
            for i in range(int(length/2)):
                if palinedrome_list[i] != palinedrome_list[length - i -1]:
                    return False
            return True