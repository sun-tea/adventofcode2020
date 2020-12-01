data = []
with open("inputs/day1.txt") as f:
    for number in f:
        data.append(int(number))

target = 2020
for x in data:
    remainder = target - x
    if remainder in data:
        print(remainder * x)
        exit(0)
