#file = open("./Day 7/Day7Input.txt", "r")
file = open("./Day 7/TestInputDay7.txt", "r")

input = file.readlines()
#print(input)

top_level_dir = dict()
current_dir = dict()
previous_dir_key = list()
move_index = 0

for index, line in enumerate(input):
    
        computer_input = line.strip().split(" ")
        #print()
        #print("Line", computer_input, index)
        
        low_level_dir = {}
        
        if computer_input[1] == "cd" and computer_input[2] != "..":
            previous_dir_key.append(computer_input[2])
        #     if len(previous_dir_key) > 2:
        #         previous_key = previous_dir_key[-2]
        #         print("previous key", previous_dir_key, previous_key)
        # if computer_input[1] == "cd" and computer_input[2] == "..":
        #     if len(previous_dir_key) > 3:
        #         previous_key = previous_dir_key[-3] 
        #         print("one dir up:", previous_key)
                
        if computer_input[1] == 'ls':
            low_level_dir = {}
        
        if computer_input[1] == "cd" and computer_input[2] != "..":
        #if index == 0:
            top_level_dir[computer_input[2]] = {}
            current_dir = top_level_dir
        #if index > 0:
                
            # if computer_input[1] == "cd":
            #     low_level_dir = {}
            #     if computer_input[2] in top_level_dir[list(top_level_dir.keys())[0]]:
            #         print(computer_input, top_level_dir[list(top_level_dir.keys())[0]][computer_input[2]])
            #         low_level_dir[computer_input[2]] = {}
                    
                    
            # if computer_input[0] == "dir":
            #     low_level_dir[computer_input[1]] = {}
            #     top_level_dir[list(top_level_dir.keys())[-1]].update(low_level_dir)
                    
            # if computer_input[0].isnumeric():
            #     low_level_dir[computer_input[1]] = int(computer_input[0])
            #     print(computer_input, low_level_dir)
            #     top_level_dir[list(top_level_dir.keys())[-1]].update(low_level_dir)
            
        
        if computer_input[0] == "dir": 
            low_level_dir[computer_input[1]] = {}
            print("directory:", current_dir)
            if computer_input[1] not in list(current_dir[list(current_dir.keys())[-1]]):
            # # if computer_input[1] not in top_level_dir[list(top_level_dir.keys())[0]]:
            # #     print("no keys")
                current_dir[list(current_dir.keys())[0]][computer_input[1]] = {}
                
            if computer_input[1] in current_dir[list(current_dir.keys())[-1]]:
                print("keys!", computer_input)
                #print("top_level_dir:", top_level_dir[list(top_level_dir.keys())][0])
                #top_level_dir[list(top_level_dir.keys())[0]][computer_input[1]].update(low_level_dir)
                
        if computer_input[0].isnumeric():
            print("current dir", current_dir.keys())
            low_level_dir[computer_input[1]] = int(computer_input[0])
            current_dir[list(current_dir.keys())[-1]].update(low_level_dir)
            
        if computer_input[1] == "cd" and index > 0 and computer_input[2] != '..':
            # current_dir = current_dir[computer_input[previous_dir_key[-1]]]
            print("current dir keys", current_dir[list(current_dir.keys())[0]][computer_input[2]])
        
            
        if computer_input[1] == "cd" and index > 0 and computer_input[1] == '..':
            move_index += 1
            print(previous_dir_key[-move_index])
        

  


        
#recur_command(index=index, line_command=computer_input, top_level_dir=top_level_dir)

 
print()
print("top level:", top_level_dir)
        