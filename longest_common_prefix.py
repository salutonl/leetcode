class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lengthOfList = len(strs)
        if len(strs) == 0:
            return ''
        first = strs[0]
        lenOfFisrt = len(first)
        common = ''
        for i in range(lenOfFisrt):
            prefix = common + first[i]
            for j in range(lengthOfList):
                if len(common) == len(strs[j]):
                    return common
                if strs[j][i] != first[i]:
                    return common
            common = prefix
        return common
