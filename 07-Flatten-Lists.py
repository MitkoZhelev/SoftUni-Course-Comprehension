element = input().split("|")
sequences = []
sequences = [
            [int(element) for element in seq.split(" ")
                if element.isnumeric()]
              for seq in element]

sequences.reverse()
sequences = [num for row in sequences for num in row]
print(' '.join([str(x) for x in sequences]))