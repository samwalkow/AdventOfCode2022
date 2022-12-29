#file = open("./Day 7/Day7Input.txt", "r")
file = open("./Day 7/TestInputDay7.txt", "r")

input = file.readlines()
#print(input)

flag = False
top_dir = dict()
current_dir = dict()
local_dict = dict()

for index, line in enumerate(input):

    computer_input = line.strip().split(" ")
    #print(computer_input)
    
    if computer_input[1] == 'cd' and index == 0:
        top_dir[computer_input[2]] = {}
        current_dir = top_dir
        
    if computer_input[0] == 'dir':
        local_dict[computer_input[1]] = {}
        #print(local_dict)
        
    if computer_input[0].isnumeric():
        local_dict[computer_input[1]] = int(computer_input[0])
        #print(local_dict)
        
    if computer_input[1] == 'cd' and index > 0:
        print(local_dict, current_dir)
        previous_key = list(current_dir.keys())[0]
        current_dir[list(current_dir.keys())[0]].update(local_dict)
        print(current_dir)
        current_dir = local_dict
        local_dict = dict()
        
print(top_dir)
        
    
    