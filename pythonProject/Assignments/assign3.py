# Student Number: 251214226
# Student Name: Jarry Wu

def add_to_list(to_do_list):
    '''
    Adds items to a to-do list
    :param to_do_list: the list to add to
    :return: None
    '''
    input_repeat = True
    if to_do_list:
        print("Here is the list\n")
        for task in to_do_list:
            print(task.strip())
    else:
        print("The list is empty")
    to_do_list.append(input("\nWhat would you like to add?\n"))
    # Repeats input prompt until user enters '', which exits while loop
    while input_repeat:
        add_to_do_list = input("What else would you like to add to the list? (Press Enter/Return to stop)\n")
        if add_to_do_list == '':
            input_repeat = False
        else:
            to_do_list.append(add_to_do_list)
    print("Here is the list with your new items:\n")
    for task in to_do_list:
        print(task.strip())


def completed_item(to_do_list):
    '''
    Mark an item from a to-do list as completed
    :param to_do_list: the list that contains the item that was completed
    :return: None
    '''
    input_repeat = True
    print("This is the chosen list\n")
    for task in to_do_list:
        print(task.strip())
    complete = input("\nWhich item do you wish to mark as complete?\n")
    for task in to_do_list:
        # Ignoring case sensitivity, check whether the input is in the list and adds an "[x]" to it
        if task == complete or task.lower() == complete:
            to_do_list[to_do_list.index(task)] = "[x]" + task
        # Checks if the input is valid and prompts user to re-enter input if it isn't
        elif complete != "" and complete not in to_do_list:
            print("The item was not marked. Please make sure you enter an item that appears in the list")
    print("\nThis is the list after marking the item as complete:\n")
    for task in to_do_list:
        print(task)
        # While loop that repeats the above code but with different text, until user enters ''
    while input_repeat:
        complete2 = input("\nChoose another item to mark as complete. [Enter/Return when done].\n")
        for task in to_do_list:
            if task in complete2:
                to_do_list[to_do_list.index(task)] = "[x]" + task
                print("This is the list after marking the item as complete:\n")
                for element in to_do_list:
                    print(element)
            # Checks if the input is valid and prompts user to re-enter input if it isn't
            elif complete2 != "" and complete2 not in to_do_list:
                print("The item was not marked. Please make sure you enter an item that appears in the list")
            elif complete2 == "":
                input_repeat = False


def create_to_do_list(list_name, full_list):
    '''
    Creates a new to-do list from a file or through user input
    :param list_name: the to-do list's name: Today, Someday, Completed
    :param full_list: the list of to-do lists
    :return: None
    '''
    list_creation = input("Are you creating this list from a file, or manually?\n").lower()
    if list_creation == "file":
        file_name = input("From which file are you creating the list?\n")
        file_list = open(file_name)
        # Converts file into a list and appends it to either the today list or someday list index
        if list_name == "today":
            for line in file_list:
                full_list[0].append(line.strip())
        else:
            for line in file_list:
                full_list[1].append(line.strip())
        file_list.close()
    elif list_creation == "manually":
        # Uses add_to_list function to manually create lists in today or someday list
        if list_name == "today":
            add_to_list(full_list[0])
        else:
            add_to_list(full_list[1])
    # If user inputs something other than "file" or "manually," exit the function
    else:
        print("Sorry. We can't create a list that way.")
        return None
    print("\nThank you for creating a to-do list!")


def edit_to_do_list(to_do_list):
    '''
    Edits items in a to-do list
    :param to_do_list: the list to edit
    :return: None
    '''
    input_repetition = True
    print("Here is the list you would like to edit\n")
    for task in to_do_list:
        print(task.strip())
    changing_item = input("\nWhat item would you like to edit?\n")
    changer_item = input("What would you like to change this item to?\n")
    # Finds the index of the item being changed and replaces it with the new item
    to_do_list[to_do_list.index(changing_item)] = changer_item
    # Loops the previous code with different input text
    while input_repetition:
        changing_item2 = input("Choose another item to edit. [Return/Enter when done]\n")
        if changing_item2 == "":
            # If user inputs "" immediately exit function
            return None
        changer_item2 = input("What would you like to change this item to?\n")
        if changing_item2 in to_do_list:
            to_do_list[to_do_list.index(changing_item2)] = changer_item2
        else:
            print("Sorry. You can't edit an item that isn't in the list.")


def print_lists(all_lists):
    '''
    Prints all of the to-do lists, using different characters to delineate each list
    :param all_lists: a list containing the Today, Someday, and Completed Lists
    :return: None
    '''
    # Checks if the element in the full list is empty. If it isn't, print out each task in the proper format
    if all_lists[0]:
        print("#" * 40)
        print("TO-DO TODAY:\n")
        for task in all_lists[0]:
            print(" " * 4 + task.strip())
        print("#" * 40)
    if all_lists[1]:
        print("+" * 40)
        print("TO-DO SOMEDAY:\n")
        for task in all_lists[1]:
            print(" " * 4 + task.strip())
        print("+" * 40)
    if all_lists[2]:
        print("x" * 40)
        print("TO-DO COMPLETED:\n")
        for task in all_lists[2]:
            print(" " * 4 + task.strip())
        print("x" * 40)


def prioritize_item(to_do_list):
    '''
    Mark an item in a to-do list as having either a high or low priority
    :param to_do_list: the to-do list holding the item to be marked with a priority level
    :return: None
    '''
    input_repetition = True
    print("This is the current list\n")
    for task in to_do_list:
        print(task.strip())
    prioritize_input = input("\nWhich item would you like to prioritize?\n")
    # Checks if input can be found in the to-do list and if not, re-prompt user to enter new item
    while input_repetition:
        if prioritize_input.strip() not in to_do_list:
            print("Sorry. But you can't prioritize something that isn't in the list.")
            prioritize_input = input("Which item would you like to prioritize?\n")
        else:
            input_repetition = False
    priority_level = input("Which level of priority? [Options: High, Low]\n").lower()
    if priority_level == "high":
        # Finds the index of the item and replaces it with a copy containing the proper priority marking
        to_do_list[to_do_list.index(prioritize_input)] = prioritize_input + "!!"
    elif priority_level == "low":
        to_do_list[to_do_list.index(prioritize_input)] = prioritize_input + "--"
    input_repetition = True
    # Repeats the code above but with different input text
    while input_repetition:
        prioritize_input2 = input("Choose another item to prioritize. [Enter/Return when done]\n")
        if prioritize_input2 != "" and prioritize_input2 not in to_do_list:
            print("Sorry. But you can't prioritize something that isn't in the list.")
        elif prioritize_input2 == "":
            input_repetition = False
        else:
            priority_level2 = input("Which level of priority? [Options: High, Low]\n").lower()
            if priority_level2 == "high":
                to_do_list[to_do_list.index(prioritize_input2)] = prioritize_input2 + "!!"
            elif priority_level2 == "low":
                to_do_list[to_do_list.index(prioritize_input2)] = prioritize_input2 + "--"

    print("This is your prioritized list:\n")
    for task in to_do_list:
        print(task.strip())


def remove_completed(full_list):
    '''
    Removes any items that have been marked as completed in any to-do list, counting
    how many items are removed from each to-do list. It adds all of the removed items
    to the Completed list, removing the [x] from the item before adding it
    :param full_list: a list containing the Today, Someday, and Completed Lists
    :return: a list containing how many items were removed from each list
    '''
    # Variables used to track the number of tasks removed from each list
    today_removed = 0
    someday_removed = 0
    removed_list = []
    # Checks if the "today" to-do list is filled, removes completed elements, and appends them to the completed list
    if full_list[0]:
        for element in full_list[0]:
            if element.startswith("[x]"):
                full_list[0].remove(element)
                full_list[2].append(element.strip("[x]"))
                today_removed += 1
    # Checks if the "someday" to-do list is filled, removes completed elements, and appends them to the completed list
    if full_list[1]:
        for element in full_list[1]:
            if element.startswith("[x]"):
                full_list[1].remove(element)
                full_list[2].append(element.strip("[x]"))
                someday_removed += 1
    removed_list.append(today_removed)
    removed_list.append(someday_removed)
    return removed_list


def sort_list(to_do_list):
    '''
    Sort a to-do list, considering priority and completion when ordering
    :param to_do_list: the to-do list to be sorted
    :return: None
    '''
    # Create 4 new lists to be used for sorting
    high_priority_list = []
    no_priority_list = []
    low_priority_list = []
    completed_list = []
    for element in to_do_list:
        # Checks if element is high priority and incomplete and adds to the proper new list
        if "!!" in element and not element.startswith("[x]"):
            high_priority_list.append(element)
        # Checks if element is low priority and incomplete and adds to the proper new list
        elif "--" in element and not element.startswith("[x]"):
            low_priority_list.append(element)
        # Checks if element is completed and adds to the proper new list
        elif element.startswith("[x]"):
            completed_list.append(element)
        # Adds all remaining tasks into the no priority list
        else:
            no_priority_list.append(element)
    # Clears old to-do list to add a properly ranked and sorted version of the lists using list operations
    to_do_list.clear()
    to_do_list.extend(sorted(high_priority_list) + sorted(no_priority_list) + sorted(low_priority_list) + sorted(completed_list))


def validate_option(option):
    '''
    Checks if the user has entered a valid choice. If it is invalid,
    loop until it is valid or 'done'
    :param option: the user's choice (a string)
    :return: True, if valid
             False, if done
    '''
    valid_options = ["add", "completed", "create", "done", "edit", "export", "prioritize", "remove", "sort", "view"]
    # Checks if the users input is part of the valid options available
    if option in valid_options:
        return True
    else:
        print("That input is invalid. Please try again.")
        return False


def which_list(list_name, full_list):
    '''
    Checks the to-do list's name, and returns the corresponding list
    :param list_name: the name of the list being looked for
    :param full_list: a list containing the Today, Someday, and Completed Lists
    :return: the Today, Someday, Complete, or All lists
             None, otherwise
    '''
    # Takes user input and returns the appropriate list from the list_of_lists
    if list_name == "today":
        return full_list[0]
    elif list_name == "someday":
        return full_list[1]
    elif list_name == "completed":
        return full_list[2]
    else:
        return full_list


def write_to_file(to_do_list):
    '''
    Exports a to-do list to a file
    :param to_do_list: the list to be exported
    :return: None
    '''

    file = input("What file would you like to write to?\n")
    write_file = open(file, 'w')

    # write to file in such a way that last line doesn't include newline character
    for item in to_do_list:
        if to_do_list.index(item) == len(to_do_list) - 1:
            write_file.write(item)
        else:
            write_file.write(item + '\n')
    write_file.close()


def main():
    '''
    Runs a program for creating, modifying, and exporting to-do lists.
    :return: None
    '''
    list_of_lists = [[], [], []]
    chosen_list = input("Choose a list to create. [Options: Today, Someday]\n").lower()
    create_to_do_list(chosen_list, list_of_lists)
    action_call = input("\nWhat would you like TO-DO? [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view]\n").lower()
    # Uses validate_option function to loop until user inputs a valid option
    while not validate_option(action_call):
        action_call = input("What would you like TO-DO? [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view]\n").lower()
        validate_option(action_call)
    # Loops for user input and calls the appropriate function for each option until user enters "done."
    while action_call != "done":
        if action_call == "add":
            selected_list = input("Which list would you like to add to? [Options: Today, Someday]\n").lower()
            add_to_list(which_list(selected_list, list_of_lists))
            action_call = input("\nWould you like to do something else? [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view]\n").lower()

        elif action_call == "completed":
            selected_list = input("Which list contains items you would like to mark as complete? [Options: Today, Someday]\n").lower()
            completed_item(which_list(selected_list, list_of_lists))
            action_call = input("Would you like to do something else? [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view]\n").lower()

        elif action_call == "create":
            selected_list = input("Which list would you like to create? [Options: Today, Someday]\n").lower()
            create_to_do_list(selected_list, list_of_lists)
            action_call = input("\nWould you like to do something else? [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view]\n").lower()

        elif action_call == "edit":
            selected_list = input("Which list would you like to edit? [Options: Today, Someday]\n").lower()
            edit_to_do_list(which_list(selected_list, list_of_lists))
            action_call = input("Would you like to do something else? [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view]\n").lower()

        elif action_call == "export":
            selected_list = input("Which list would you like to export? [Options: Today, Someday]\n").lower()
            write_to_file((which_list(selected_list, list_of_lists)))
            action_call = input("\nWould you like to do something else? [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view]\n").lower()

        elif action_call == "prioritize":
            selected_list = input("Which list would you like to add priorities to? [Options: Today, Someday]\n").lower()
            prioritize_item(which_list(selected_list, list_of_lists))
            action_call = input("\nWould you like to do something else? [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view]\n").lower()

        elif action_call == "remove":
            # Assigns returned list to a variable and uses f strings to print each element in the list separately
            result = remove_completed(list_of_lists)
            print(f'{result[0]} removed from #Today# list.')
            print(f'{result[1]} removed from +Someday+ list.')
            action_call = input("\nWould you like to do something else? [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view]\n").lower()

        elif action_call == "sort":
            selected_list = input("Which list would you like to sort?\n").lower()
            sort_list(which_list(selected_list, list_of_lists))
            action_call = input("\nWould you like to do something else? [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view]\n").lower()

        elif action_call == "view":
            # Creates a copy of the list_of_lists that can be used in the print_lists function to print specific lists
            # without changing the original list_of_lists
            copy_full_list = [[], [], []]
            selected_list = input("Which list would you like to view? [Options: Today, Someday, Completed, ALL]\n").lower()
            if selected_list == "today":
                for element in list_of_lists[0]:
                    copy_full_list[0].append(element)
            elif selected_list == "someday":
                for element in list_of_lists[1]:
                    copy_full_list[1].append(element)
            elif selected_list == "completed":
                for element in list_of_lists[2]:
                    copy_full_list[2].append(element)
            else:
                copy_full_list = list_of_lists
            print_lists(copy_full_list)
            action_call = input("\nWould you like to do something else? [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view]\n").lower()
    print("Get it done!")
    print_lists(list_of_lists)


main()
