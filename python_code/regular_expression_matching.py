class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        elif not s or not p:
            return False
        flag = 0
        n_recog_s = 0
        number_j = 0
        number_p = 0
        for i in s:
            for j in p[flag:]:
                if i == j:
                    flag += 1
                    number_p += 1
                    n_recog_s += 1
                    number_j += 1
                    break
                elif j == '.':
                    flag += 1
                    n_recog_s += 1
                    number_j += 1
                    number_p += 1
                    break
                elif j == '*':
                    
                    if p[number_j - 1] == i:
                        if flag + 1 == len(s):
                            number_p += 1
                        n_recog_s += 1
                        break
                    elif p[number_j - 1] == '.':
                        if flag + 1 == len(s):
                            number_p += 1
                        n_recog_s += 1
                        break
                    else:
                        flag += 1
                        number_j += 1
                        number_p += 1
                else:
                    flag += 1
                    number_j += 1
                    number_p += 1

        return True if n_recog_s == len(s) and number_p == len(p) else False

res = Solution()
re = res.isMatch("aa",
            "a*")
print(re)
