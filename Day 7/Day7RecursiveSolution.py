#file = open("./Day 7/Day7Input.txt", "r")
file = open("./Day 7/TestInputDay7.txt", "r")

input = file.readlines()
#print(input)

top_dir = dict()
current_dir = dict()
previous_key = str()
previous_keys = list()
move_count = 1      # set to one, because I want to offset the indexing. I want the next level up. 

visited = [] # List for visited nodes.
queue = []     #Initialize a queue
count_dir = 0
sum_dir = dict()
all_keys = set()

def bfs(visited: list, graph: dict, node: str, count: int): #function for BFS
    visited.append(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
        m = queue.pop(0) 
        #print (m, end = " ") 

    for key, neighbour in graph[m].items():
        #print(key, neighbour, type(neighbour))
        if isinstance(neighbour, int):
            count += neighbour
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
           
            print(key, neighbour, count)
        #print(key, neighbour, count)
    #print(key, neighbour, count)
        


def find_values(dictionary: dict, search: bool, keys: str = None) -> dict:
    
    if search is True:
        for keys_in_dict in dictionary.keys():
            if keys != keys_in_dict:
                #print("wrong level", keys, keys_in_dict, dictionary.keys())
                return find_values(dictionary= dictionary[keys_in_dict], search=True, keys=keys)
            if keys == keys_in_dict:
                #print("keys!", keys, keys_in_dict, dictionary.keys())
                if keys == '/':
                    return top_dir
                return dictionary[keys]
            
    # if search is False:
    #      #print(keys, dictionary)
    #      for keys_in_dict in dictionary.keys():
            
    #         if keys != keys_in_dict:
    #             #print("wrong level", keys, keys_in_dict, dictionary.keys())
    #             return find_values(dictionary= dictionary[keys_in_dict], search=False, keys=keys)
    #         if keys == keys_in_dict:
    #             #print("keys!", keys, keys_in_dict, dictionary.keys())
    #             # if keys == '/':
    #             #     return top_dir
    #             # return dictionary[keys]
    #             print(keys)
        
    # else:
    #     for flag, values in dictionary.items():
    #         print(flag, type(flag), values)
    #         # how to cout up and move up the tree? I can count and move down easier, not so easy when moving up
    #         # start a new dict that keeps the keys and has the counts for values?
    #         if isinstance(values, dict) and len(values) > 1:
    #            #print(flag, values)
    #             for f, v in values.items():
    #                 if isinstance(v, int):
    #                     print(f, v)
    #                     dir_sum += v
    #                     print("sum", dir_sum)
    #             find_values(dictionary=values, search=False)
    #         if isinstance(values, dict) and len(values) == 1:
    #             low_flag = list(values.keys())[0]
    #             dir_sum += values[low_flag]
    #             print("sum", dir_sum)
    #             find_values(dictionary=values, search=False)
    #         if dir_sum <= 100000:
    #             return dir_sum            
        
for index, line in enumerate(input):
    
    computer_input = line.strip().split(" ")
    #print("Line", computer_input)
    
    local_dir = dict()
    
    if computer_input[1] == "cd":
        count_dir = 0
        
        if index == 0:
            top_dir[computer_input[2]] = {}
            current_dir = top_dir
            sum_dir = current_dir
            previous_key = computer_input[2]
            previous_keys.append(computer_input[2])
            all_keys.add(computer_input[2])
        if computer_input[2] != '..' and index > 0:
            # print(previous_key, current_dir)
            current_dir = current_dir[previous_key] # reset current dir to the next level down
            previous_key = computer_input[2]        # reset previous key to be the new key
            previous_keys.append(computer_input[2])
            all_keys.add(computer_input[2])
        if computer_input[2] == '..' and index > 0:
            # for some reason this isn't moving the current dir to include the 'd' key
            move_count += 1
            previous_key = previous_keys[-move_count] # here is the right key, but how to get to the right level?
            # move back up the tree to find the right dict; we are too far down the tree right now
            current_dir = find_values(dictionary=top_dir, search=True, keys=previous_key, )
            #print("current dir:", current_dir)
            previous_key =  previous_keys[-move_count]  # resest previous key from the level down
            
    if computer_input[0] == "dir":
        local_dir[computer_input[1]] = {}
        current_dir[previous_key].update(local_dir)
        all_keys.add(computer_input[1])
        
    if computer_input[0].isnumeric():
        #print(previous_key, current_dir)
        local_dir[computer_input[1]] = int(computer_input[0])
        current_dir[previous_key].update(local_dir)
        count_dir += int(computer_input[0])
        #print(current_dir[previous_key], count_dir)
    
    # print("local dir:", local_dir)
print("top dir:", top_dir)   
print()
#print(all_keys)
#print("Sum:", count_dir)
#print("Sum:", find_values(dictionary=top_dir, search=False))  

# Driver Code
#print("Following is the Breadth-First Search")
bfs(visited=visited, graph=top_dir, node='/', count=count_dir)    # function calling  

# for dir in all_keys:
#     find_values(search=False, keys=dir, dictionary=top_dir)