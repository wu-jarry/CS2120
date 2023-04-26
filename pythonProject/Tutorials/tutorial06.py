# Jarry Wu

######################### INSERT YOUR CODE BELOW #########################

# 1 - define the different_alpha() function
def different_alpha(file_name, letter):
    word_list = open(file_name)
    words = word_list.read()
    my_list = words.split("\n")
    my_list_sorted = sorted(my_list)
    letter_list = []
    for words in reversed(my_list_sorted):
        if letter in words and words.startswith(letter):
            letter_list.insert(0, words)
            my_list_sorted.remove(words)
    letter_list_sorted = sorted(letter_list)
    my_list_letter_list = letter_list_sorted + my_list_sorted
    word_list.close()
    return my_list_letter_list

# 2 - define the main() function


def main():
    file_name = input("Please input a filename \n")
    letter = input("Please input a letter to sort for \n")
    print(different_alpha(file_name, letter))

# 3 - don't forget to call main()!


main()

######################### INSERT YOUR CODE ABOVE #########################
