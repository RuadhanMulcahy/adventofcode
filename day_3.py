import string

def create_priorities_lookup():
    priorities_lookup = dict.fromkeys(string.ascii_lowercase, 0)
    priorities_lookup = priorities_lookup | dict.fromkeys(string.ascii_uppercase, 0)

    for idx, item in enumerate(priorities_lookup):
        priorities_lookup[item] = idx + 1

    return priorities_lookup

def split(bag):
    pivot = (len(bag) + 1) // 2
    compartment_1 = bag[0:pivot]
    compartment_2 = bag[pivot:]
    return compartment_1, compartment_2

def item_in_both(compartment_1, compartment_2):
    compartment_1_lookup = {}

    for item in compartment_1:
        compartment_1_lookup[item] = None

    for item in compartment_2:
        if item in compartment_1_lookup:
            compartment_1_lookup.clear()
            return item

# Part 1

priorities_sum = 0
priorities_lookup = create_priorities_lookup()

with open('input.txt', 'r') as file:
    for line_num, bag in enumerate(file):
        compartment_1, compartment_2 = split(bag.strip()) 
        item = item_in_both(compartment_1, compartment_2)
        priorities_sum += priorities_lookup[item]

# ****************************** Part 2 *****************************

bags = []
priorities_sum = 0

with open('input.txt', 'r') as file:
    for bag in file:
        bags.append(bag.strip())

for idx in range(0, len(bags), 3):
    bag_1 = dict.fromkeys(bags[idx], 0)
    bag_2 = dict.fromkeys(bags[idx+1], 0)
    bag_3 = dict.fromkeys(bags[idx+2], 0)

    for item in bag_1:
        if item in bag_2 and item in bag_3:
            priorities_sum += priorities_lookup[item]

print(priorities_sum)

