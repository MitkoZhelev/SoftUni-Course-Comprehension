size = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(size)]

first_diagonal = [matrix[i][i] for i in range(size)]

second_diagonal = [matrix[i][size - i - 1] for i in range(size)]

print(f'First diagonal: {", ".join([str(x) for x in first_diagonal])}. Sum: {sum(first_diagonal)}')
print(f'Second diagonal: {", ".join([str(x) for x in second_diagonal])}. Sum: {sum(second_diagonal)}')

