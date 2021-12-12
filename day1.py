# Day 1 - Advent of Code 2021


# Part One
file = open("day1.txt", 'r')
contents = file.read()

content_list = contents.splitlines()
prev_num = int(content_list[0])
count = 0

for number in content_list[1:]:
    count += 1 if int(number) > prev_num else 0
    prev_num = int(number)

print("Part One:", count) # 1564


# Part Two

# Convert strings to int
measurements = [int(number) for number in content_list]

count = 0
prev_measurement = sum(measurements[:3])

for i in range(1, 1998):
    measurement = sum(measurements[i:i+3])
    count += 1 if measurement > prev_measurement else 0
    prev_measurement = measurement

print(f"Part Two: {count}")
