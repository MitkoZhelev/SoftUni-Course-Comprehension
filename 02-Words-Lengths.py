words = input().split(", ")


full_dict = [f'{word} -> {len(words)}' for word in words]


print(", ".join(full_dict))