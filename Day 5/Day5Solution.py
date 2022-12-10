#file = open("./Day 5/TestDay5Input.txt")
file = open("./Day 5/Day5Input.txt")

input = file.readlines()

crate_map = dict()
position_map = dict()
top_crates = str()

for line in input:
    if line.startswith(" 1"):
        for char in line:
            if char.isnumeric():
                position_map[int(char)] = line.index(char)
                crate_map[int(char)] = []
             
for line in input:
    crate_key = int()
    for idx, char in enumerate(line):
        if char.isalpha():
            # print(idx, char,  line.index(char))
            crate_key = list(position_map.values()).index(idx)+1
            crate_map[crate_key] += char
    if len(line.strip()) == 0:
        break

for key, value in crate_map.items():
    value.reverse()
    
for line in input:
    if line.startswith("m"):
        line_list = line.split()
        move_list = [char for char in line_list if char.isnumeric()]
        num_to_move = int(move_list[0])
        source_stack = int(move_list[1])
        target_stack = int(move_list[2])
        for number in list(range(1, num_to_move+1)):
            crates_to_move = crate_map[source_stack][-1]
            crate_map[source_stack].pop()
            crate_map[target_stack] += crates_to_move
            print()
            for key, value in crate_map.items():                 
                print(key, value) 
        

for key, value in crate_map.items():                 
    print(key, value) 
    top_crates += value[-1]

print()    
print("List of crates at the top:", top_crates)
   