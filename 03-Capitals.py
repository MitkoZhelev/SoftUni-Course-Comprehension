countires = input().split(", ")
capitals = input().split(", ")

full_list = {key:value for key,value in zip(countires,capitals)}

[print(f'{key} -> {value}')for key, value in full_list.items()]