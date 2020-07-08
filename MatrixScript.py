# This my entire solution to the HackerRank regex and parsing matrix script challenge

import re
rows, columns = map(int, input().split())
    script = []

    for _ in range(rows):
        matrix_item = input()
        script.append(matrix_item)

    em = ''
    for i in range(columns):
        for row in script:
            em += row[i]
    print(re.sub(r'(?<=\w)[!@#$% ]+(?=\w)', ' ', em))
