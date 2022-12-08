# Part 1:

file = "Day 4/Day4Input.txt"

input = open(file)

test_pair = "2-8,3-7"

count_fully_contained_pairs = 0
partially_contained_pairs = 0
no_contained_pairs = 0
all_lines_count = 0

    
for line in input:
    
    all_lines_count += 1
    
    first_pair, second_pair = line.strip().split(",")

    first_range_start, first_range_stop = first_pair.split("-")
    second_range_start, second_range_stop = second_pair.split("-")

    first_start = int(first_range_start)
    first_stop = int(first_range_stop)
    second_start = int(second_range_start)
    second_stop = int(second_range_stop)
    
    first_range = list(range(int(first_range_start), int(first_range_stop)+1))
    second_range = list(range(int(second_range_start), int(second_range_stop)+1))
        
    first_set = set(first_range)
    second_set = set(second_range)
    range_intersection = first_set.intersection(second_set)
    if len(range_intersection) == 0:
        no_contained_pairs += 1
    if len(range_intersection) > 0:
        #if len(second_set) != len(range_intersection) and len(first_set) != len(range_intersection):
        partially_contained_pairs += 1
    if (len(second_set) == len(range_intersection)) or (len(first_set) == len(range_intersection)) :
        count_fully_contained_pairs += 1
 
print()  
print("No overlap:", no_contained_pairs)      

# Part 1 Answer:   
print("Full overlap:", count_fully_contained_pairs)

# Part 2 Answer:
print("Partial overlap:", partially_contained_pairs)
print("Total Number of Lines:", all_lines_count)



