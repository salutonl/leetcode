def romanToInt(self, s: str) -> int:
    result = 0
    previous_character = 0
    dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    reversed_string = s[::-1]
    for string in reversed_string:
        if dict[string] >= previous_character:
            result += dict[string]
        else:
            result -= dict[string]
        previous_character = dict[string]
    return result