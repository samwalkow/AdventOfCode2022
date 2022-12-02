# Instructions:
# The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

# For example, suppose the Elves finish writing their items' Calories and end up with the following list:

# 1000
# 2000
# 3000

# 4000

# 5000
# 6000

# 7000
# 8000
# 9000

# 10000

# This list represents the Calories of the food carried by five Elves:

#     The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
#     The second Elf is carrying one food item with 4000 Calories.
#     The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
#     The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
#     The fifth Elf is carrying one food item with 10000 Calories.

# In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

with open("./Day1Input.txt") as f:
    input_data = f.readlines()
    #
# print(input_data)

highest_calorie_count = 0
elf_calorie_count = 0

for line in input_data:
    if line != '\n':
        line_num = int(line.strip())
        elf_calorie_count += line_num
    if line == '\n':
        # print("blank line")
        elf_calorie_count = 0
    if elf_calorie_count > highest_calorie_count:
        highest_calorie_count = elf_calorie_count
    print("elf count:", elf_calorie_count)
    print("highest count so far:", highest_calorie_count)
    
    
print("highest count:", highest_calorie_count)
print()

# Defintion approach

from typing import List

def get_data(file):
    """Load a text file and get input data. 

    Args:
        file (text file): the input file to be parsed, put in a list, and returned

    Returns:
        List: Return a list of of strings, with each string being a line of input
    """
    with open(file) as f:
        input_data = f.readlines()
        return input_data
    
def count_calories(input_data: List[str]) -> int:
    """A function to take input as a list, convert string input to integrers, and count up each line to find the highest count possible. 

    Args:
        input_data (List[str]): Input data as list with strings that represent numbers

    Returns:
        int: the highest number of calories per elf
    """
    
    highest_calorie_count = 0
    elf_calorie_count = 0

    for line in input_data:
        if line != '\n':
            line_num = int(line.strip())
            elf_calorie_count += line_num
        if line == '\n':
        # print("blank line")
            elf_calorie_count = 0
        if elf_calorie_count > highest_calorie_count:
            highest_calorie_count = elf_calorie_count
        print("elf count:", elf_calorie_count)
        print("highest count so far:", highest_calorie_count)
    return highest_calorie_count
    
    
print("highest count:", count_calories(get_data("./Day1Input.txt")))
print()

# Part Two Instructions:

# By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

# To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

# In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

# Completely procedural approach:
# with open("./Day1Input.txt") as f:
#     input_data = f.readlines()
#     #
# # print(input_data)

# highest_calorie_count = list()
# elf_calorie_count = 0

# for line in input_data:
#     if line != '\n':
#         line_num = int(line.strip())
#         elf_calorie_count += line_num
#     if line == '\n':
#         # print("blank line")
#         elf_calorie_count = 0
#     #if elf_calorie_count > highest_calorie_count:
#     highest_calorie_count.append(elf_calorie_count)
#     # print("elf count:", elf_calorie_count)
#     # print("highest count so far:", highest_calorie_count)
    
# highest_three_calorie_elves = sorted(highest_calorie_count)[-3:]
# print(sum(highest_three_calorie_elves))
    
    
# Defintions Approach:

from typing import List

def get_data(file):
    """Load a text file and get input data. 

    Args:
        file (text file): the input file to be parsed, put in a list, and returned

    Returns:
        List: Return a list of of strings, with each string being a line of input
    """
    with open(file) as f:
        input_data = f.readlines()
        return input_data
    
def count_calories(input_data: List[str]) -> int:
    """A function to take input as a list, convert string input to integrers, and count up each line to find the highest count possible. 

    Args:
        input_data (List[str]): Input data as list with strings that represent numbers

    Returns:
        int: the highest number of calories per elf
    """
    
    highest_calorie_count = list()
    elf_calorie_count = 0

    for line in input_data:
        if line != '\n':
            line_num = int(line.strip())
            elf_calorie_count += line_num
        if line == '\n':
            elf_calorie_count = 0
        highest_calorie_count.append(elf_calorie_count)
    return highest_calorie_count
    
def calorie_total_sort(highest_calorie_count: List[int]) -> int:
    """Sort and return the count of the three highest values in the list.

    Args:
        highest_calorie_count (List[int]): a list of numbers thtat represent calorie counts

    Returns:
        int: a total of the highest three calorie counts
    """
    highest_three_calorie_elves = sum(sorted(highest_calorie_count)[-3:])
    return highest_three_calorie_elves

print(calorie_total_sort(count_calories(get_data("./Day1Input.txt"))))


# Class Approach

# I can't think of what the class attributes would be? All the 'methods' are functions that need to be chained together. I don't think a class is the right tool for this job. 

# from typing import List

# class Calorie_Counter:
    
#     def __init__(self) -> None:
#         pass
    
#     def parse_file(file) -> List[str]:
#         """Load a text file and get input data. 

#         Args:
#             file (text file): the input file to be parsed, put in a list, and returned

#         Returns:
#             List: Return a list of of strings, with each string being a line of input
#         """
        
#         with open(file) as f:
#             input_data = f.readlines()
#             return input_data
        
#     def count_calories(input_data: List[str]) -> int:
#         """A function to take input as a list, convert string input to integrers, and count up each line to find the highest count possible. 

#         Args:
#             input_data (List[str]): Input data as list with strings that represent numbers

#         Returns:
#             int: the highest number of calories per elf
#         """
        
#         highest_calorie_count = list()
#         elf_calorie_count = 0

#         for line in input_data:
#             if line != '\n':
#                 line_num = int(line.strip())
#                 elf_calorie_count += line_num
#             if line == '\n':
#                 elf_calorie_count = 0
#             highest_calorie_count.append(elf_calorie_count)
#         return highest_calorie_count
        
#     def calorie_total_sort(highest_calorie_count: List[int]) -> int:
#         """Sort and return the count of the three highest values in the list.

#         Args:
#             highest_calorie_count (List[int]): a list of numbers thtat represent calorie counts

#         Returns:
#             int: a total of the highest three calorie counts
#         """
#         highest_three_calorie_elves = sum(sorted(highest_calorie_count)[-3:])
#         return highest_three_calorie_elves


# Some_input = Calorie_Counter.count_calories()

