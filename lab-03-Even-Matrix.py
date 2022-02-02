
names = [x for x in input().split(" ") ]

names_filtered = [x for x in names if len(x) % 2 == 0]
for i in range (len(names_filtered)):
    print("".join(names_filtered[i]))
