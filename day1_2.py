data = []
with open("inputs/day1.txt") as f:
    for number in f:
        data.append(int(number))

target = 2020

for i, item1 in enumerate(data):
    remainder1 = target - item1
    for j, item2 in enumerate(data[i+1:]):
        remainder2 = remainder1 - item2
        if remainder2 in data[j+1:]:
            print(item1 * remainder2 * item2)
            exit(0)
