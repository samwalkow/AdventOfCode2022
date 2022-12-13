file = open("./Day 6/Day6Input.txt")
#file = open("./Day 6/TestInputDay6.txt")
input = file.read()

four_numbers = list()

for index, char in enumerate(input):
    print(char)
    if len(four_numbers) < 4:
        four_numbers.append(char)
        print(four_numbers)
    if len(four_numbers) == 4:
        unique = len(set(four_numbers)) == len(four_numbers)
        if unique:
            print("all unique", four_numbers, index+1)
            break
        else:
            four_numbers = four_numbers[1:]
            four_numbers

        