def lcd(string1, string2):
    """
    :param string1:
    :param string2:
    :return:
    """
    len1 = len(string1) + 1
    len2 = len(string2) + 1
    str_matrix = [[0] * len1 for _ in range(len2)]
    for i in range(len(string2)):
        for j in range(len(string1)):
            if string2[i] == string1[j]:
                str_matrix[i + 1][j + 1] = str_matrix[i][j] + 1
            else:
                str_matrix[i + 1][j + 1] = max(str_matrix[i][j + 1], str_matrix[i + 1][j])

    return str_matrix[len2 - 1][len1 - 1]


res = lcd('abcdefg', 'bdaaeg')
print(res)
