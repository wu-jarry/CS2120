# YOUR NAME

######################### EDIT THE FUNCTIONS BELOW #########################

def task_1():
    filename = input('What file would you like to open?\n')
    final_value = 100
    line_count = 1
    no_error = True
    try:
        with open(filename, 'r') as file1:
            try:
                for line in file1:
                    value = int(line.strip())
                    print(final_value / value)
            except NameError:
                print("A(n) NameError was caught.")
                no_error = False
            except ZeroDivisionError:
                no_error = False
                print("A(n) ZeroDivisionError was caught.")
            except ValueError:
                no_error = False
                print("A(n) ValueError was caught.")
            line_count += 1
            file1.close()
            return no_error
    except FileNotFoundError:
        print("A(n) FileNotFoundError was caught.")


def task_2():

    in_file = open("input.txt", "r")
    out_file = open("output.txt", "w")
    line = in_file.read()
    words = line.split(' ')
    for word in words:
        print(word)
        out_file.write(word)
    # Close the files
    in_file.close()
    out_file.close()

######################### EDIT THE FUNCTIONS ABOVE ####################


def main():
    result = task_1()
    print(f"Task #1 returned {result}.")
    task_2()


main()
