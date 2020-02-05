# #Time limit Exceeded
# class Solution:
#     def longestPalindrome(self, s):
#         res = [s[i: j] for i in range(len(s))
#                for j in range(i + 2, len(s) + 1)]

#         s_dict = {}
#         for x in res:
#             s_dict.setdefault(len(x), []).append(x)

#         lenOfs = len(s)
#         maxOfnum = 0
#         maxOfstring = ''
#         lenOfdict = len(s_dict)

#         for i in range(lenOfdict):
#             length = lenOfs - i
#             lis_num = s_dict[length]
#             for j in range(len(lis_num)):
#                 flag = 1
#                 for k in range(length // 2):
#                     if lis_num[j][k] != lis_num[j][length - k - 1]:
#                         flag = 0
#                         break
#                 if flag == 1 and length > maxOfnum:
#                     maxOfnum = length
#                     maxOfstring = lis_num[j]
#                     return maxOfstring


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        else:
            start = 0
            length = 0
            maxstring = 0
            for i in range(len(s) - 1):
                right = i
                left = i
                while right < len(s) - 1 and s[right] == s[right+1]:
                    right = right + 1
                i = right + 1
                while right < len(s) - 1 and s[left - 1] == s[right + 1] and left > 0:
                    left -= 1
                    right += 1
                if right - left + 1 > maxstring:
                    maxstring = right - left + 1
                    start = left
            return s[start: start + maxstring]
            
        
