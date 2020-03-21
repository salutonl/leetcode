class Solution:
    def isValid(self, s: str) -> bool:
        forward_parentheses = []
        number_of_f = 0
        number_of_b = 0
        flag = 0
        if len(s)%2 == 1:
            return False
        for parentheses in list(s):
            print(parentheses)
            if parentheses == '{' or parentheses == '[' or parentheses == '(':
                number_of_f += 1
                flag = 1
                forward_parentheses.append(parentheses)
            if parentheses == '}' or parentheses == ')' or parentheses == ']':
                if flag == 0:
                    return False
                number_of_b += 1
                if parentheses == '}' and forward_parentheses[-1] != '{':
                    return False
                elif parentheses == ']' and forward_parentheses[-1] != '[':
                    return False
                elif parentheses == ')' and forward_parentheses[-1] != '(':
                    return False
                forward_parentheses.pop()
        if number_of_f != number_of_b:
            return False
        return True