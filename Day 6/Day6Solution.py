file = open("./Day 6/Day6Input.txt")
#file = open("./Day 6/TestInputDay6.txt")
input = file.read()


def find_signals(number_of_characters: int) -> int:
    """Function to find the unique combination of characters that indicate the start of signal or messge

    Args:
        number_of_characters (int): number of chacaters that indicate the beginning of a signal or message

    Returns:
        int: the number of characters that come before a signal or message
    """
    number_list = list()
    for index, char in enumerate(input):
        if len(number_list) < number_of_characters:
            number_list.append(char)
        if len(number_list) == number_of_characters:
            unique = len(set(number_list)) == len(number_list)
            if unique:
                return index+1
            else:
                number_list = number_list[1:]
                number_list

print("Part 1:", find_signals(4))
print("Part 2:", find_signals(14))
        