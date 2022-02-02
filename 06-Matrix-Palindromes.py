rows,cols = [int(x) for x in input().split(" ")]

matrix = []
base = ord('a')

for i in range (rows):
    for j in range(cols):
        firs_letter = chr(rows + base)
        second_letter = chr(rows+base+cols)

        matrix[i][j].append(f'{firs_letter}{second_letter}{firs_letter}')


print(matrix)