# Jarry Wu


#########################ENTER YOUR CODE BELOW################################

# QUESTION #1 - character_count()

def character_count(words):
    words = open(words)
    characters = 0
    for line in words:
        for letter in line.strip():
            characters += 1
    words.close()
    return characters

# QUESTION #2 - find_word()


def find_word(words, number):
    words = open(words)
    line_count = 0
    for line in words:
        line_count += 1
        if line_count == number:
            return line.strip()
    words.close()

# QUESTION #3 - main()


def main():
    input_loop = True
    words = input("Please input a filename\n")
    print(f'The number of characters in this file is {character_count(words)}')
    while input_loop is True:
        number = int(input("Please input an index\n"))
        print(f'The word at that index number is {find_word(words, number)}\n')
        re_loop = input("Would you like to input another index? y/n\n")
        if re_loop == "n":
            input_loop = False
    exit()


main()

#########################ENTER YOUR CODE ABOVE################################
