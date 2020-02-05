class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_map = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        res = [''] if digits else []
        for i in digits:
            res = [r + s for r in res for s in number_map[i]]
        return res
