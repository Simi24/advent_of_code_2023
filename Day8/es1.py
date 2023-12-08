from math import gcd

pathString = ""
nodesDict = {}

def get_next_element(current_element, direction):
    if direction == 'R':
        return nodesDict[current_element][1]
    elif direction == 'L':
        return nodesDict[current_element][0]

with open('input.txt', 'r') as file:

        for line in file:

            line = line.strip()

            if "=" not in line and len(line) > 0:
                  pathString = line
            elif len(line) > 0:
                key, value = line.split(' = ')
    
                value = value.replace('(', '').replace(')', '').replace(',', '')
    
                nodesDict[key.strip()] = [item.strip() for item in value.split()]

end_with_A_nodes = [node for node in nodesDict if node.endswith('A')]

# # Uncomment to get the solution of the first part 
# step_count = 0
# current_element = 'AAA'
# while current_element != 'ZZZ':

#     for direction in pathString:
#         step_count += 1
#         current_element = get_next_element(current_element, direction)

#         print(f"Current Element: {current_element}")

#         if current_element == 'ZZZ':
#             print("Raggiunto ZZZ")
#             break
#     else:
#         pathString += pathString
#         print(f"Input replicato: {pathString}")
# print(step_count)

def lcm_of_list(numbers):
    if len(numbers) == 0:
        return 1

    lcm = numbers[0]

    for i in range(1, len(numbers)):
        lcm = abs(lcm * numbers[i]) // gcd(lcm, numbers[i])

    return lcm

distances_A_to_Z = []

shortest_path_A = None
min_step_count_A = -1


for start_node in end_with_A_nodes:

    current_element = start_node

    step_count = 0

    while not current_element.endswith('Z'):

        for direction in pathString:
            step_count += 1
            current_element = get_next_element(current_element, direction)

            # print(f"Current Element: {current_element}")

            if current_element.endswith('Z'):
                break

    distances_A_to_Z.append(step_count)

lcm_result = lcm_of_list(distances_A_to_Z)

print(f"Steps before you're only on nodes that end with Z: {lcm_result}")