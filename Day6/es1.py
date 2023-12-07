time_distance_mapping = {}
times = []
distances = []
time_number = 0
distance_number = 0
with open('input.txt', 'r') as file:

        for line in file:

            line = line.strip()

            if "Time:" in line:
                  timesSplit = line.split(":")[1].strip().split()
                  values = [int(value) for value in timesSplit]
                  time_number = int(''.join(map(str, values)))
                  times = values
            else:
                  timesSplit = line.split(":")[1].strip().split()
                  values = [int(value) for value in timesSplit]
                  distance_number = int(''.join(map(str, values)))
                  distances = values

for i in range(len(times)):
      time_distance_mapping[times[i]] = distances[i]


rt = 1

for time, distance in time_distance_mapping.items():
    valid = 0
    for i in range(1, time):
        actualDistance = (time - i) * i
        if actualDistance > distance:
            valid += 1
    print(valid)
    rt *= valid

print(rt)

valid2 = 0
for i in range(1, time_number):
    actualDistance = (time_number - i) * i
    if actualDistance > distance_number:
        valid2 += 1
print(valid2)


