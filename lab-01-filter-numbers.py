start = int(input())
end = int(input())
numbers = [x for x in range(start,end+1)]
numbers_one_ten = [x for x in range (2,11)]

fildered_numbers = [x for x in numbers if any([x % numb for numb in numbers_one_ten])]

print(fildered_numbers)