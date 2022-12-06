## Day 3 Instructions:

# One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

# Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

# The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

# The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

# For example, suppose you have the following list of contents from six rucksacks:

# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw

#     The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
#     The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
#     The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
#     The fourth rucksack's compartments only share item type v.
#     The fifth rucksack's compartments only share item type t.
#     The sixth rucksack's compartments only share item type s.

# To help prioritize item rearrangement, every item type can be converted to a priority:

#     Lowercase item types a through z have priorities 1 through 26.
#     Uppercase item types A through Z have priorities 27 through 52.

# In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

file = open("./Day 3/Day3Input.txt")
#file = open("./Day 3/TestDay3Input.txt")

test_str = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"

#line = test_str

def half_the_string(line: str) -> tuple:
    """A function to take a string and split it in half

    Args:
        line (str): the string to be split in half

    Returns:
        tuple: a tuple with the first and second half of the string
    """
    
    line_length = len(line)
    if line_length%2 == 0:
        first_half = set(line[0:line_length//2])
        second_compartment = set(line[line_length//2:])
    else:
        first_half = set(line[0:(line_length//2+1)])
        second_compartment = set(line[(line_length//2+1):])
    return first_half, second_compartment


def find_common_char_in_halves(file) -> int:
    """Function to find the common char that is in both halves of the string, find the value assigned to it, and sum up and return the total value

    Args:
        file (_type_): a file that contains strings, one per line

    Returns:
        int: The sum of the value of the common characters
    """
    item_sum = 0
    for line_with_new_line in file:
        line = line_with_new_line.strip("\n")
        first_compartment = half_the_string(line)[0]
        second_compartment = half_the_string(line)[1]
        common_char = list(first_compartment.intersection(second_compartment))
        for index, value in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", start=1):
            if common_char[0] == value:
                item_sum += index
    return item_sum
        
print(find_common_char_in_halves(file))
    
# Part 2 Instructions

# As you finish identifying the misplaced items, the Elves come to you with another issue.

# For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves. That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack, and at most two of the Elves will be carrying any other item type.

# The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.

# Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.

# Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. So, in the above example, the first group's rucksacks are the first three lines:

# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg

# And the second group's rucksacks are the next three lines:

# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw

# In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges. In the second group, their badge item type must be Z.

# Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.

# Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

def find_common_char_in_threes(file) -> int:
    """Function to find the common char that is in both halves of the string, find the value assigned to it, and sum up and return the total value

    Args:
        file (_type_): a file that contains strings, one per line

    Returns:
        int: The sum of the value of the common characters
    """
    
    item_sum = 0
    line_list = list()

    for index, line_with_new_line in enumerate(file, start=1):
        line = line_with_new_line.strip("\n")
        line_set = set(line)
        line_list.append(line_set)
        
        if index%3 == 0:
            common_char = list(line_list[0] & line_list[1] & line_list[2])
           
            for index, value in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", start=1):
                if common_char[0] == value:
                    print(index, value)
                    item_sum += index
                    
            line_list = list()
    return item_sum
        
print(find_common_char_in_threes(file))
