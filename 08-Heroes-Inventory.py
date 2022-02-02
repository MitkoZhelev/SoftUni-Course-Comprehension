
names = input().split(", ")

inventory = {hero: {} for hero in names}

command = input()

while command != 'END':
    hero,item,quantity = input().split("-")
    if item not in inventory[hero]:


