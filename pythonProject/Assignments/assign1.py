# Student Number: 251214226
# Student Name: Jarry Wu

width = 20


def main():
    """
    Allows users to input a multiplicand and a multiplier
    and creates a grid using those values
    """
    # the following two lines take user input and convert that input to integer values
    number = int(input("Please enter a four-digit integer multiplicand: \n"))
    times = int(input("Please enter a two-digit integer multiplier: \n"))

    grid(number, times)


def block_string():
    """
    This function outputs the top and bottom walls of the rectangles
    in the grid
    """
    # Defines width_wall outside the loop, so it can be called on after it is done looping
    width_wall = ""
    for i in range(width):
        width_wall = width_wall + "#"
    print(width_wall)


def outline_string():
    """
    This function outputs an internal string for the rectangles,
    includes empty spaces and is outlined by walls
    """
    # Multiplied by empty string to move the "#" to the right side
    right_side_width = ""
    # Loops to create 18 spaces so the "#" lines up with the end of the top/bottom wall
    for i in range(width-2):
        right_side_width = right_side_width + " "
    side_walls = "#" + right_side_width + "#"
    print(side_walls)


def four_digit_number_string(number):
    """
    This function outputs a string with walls, spaces and a centred
    four-digit multiplicand
    :param number: The multiplicand
    """
    # Subtracts 13 from the width to centre the multiplicand from the left side
    multiplicand_left_side = "#" + " " * int(width - 13)
    # Prints 7 empty strings to centre the multiplicand from the right side
    multiplicand_right_side = " " * int(width - 13) + "#"
    print(multiplicand_left_side + str(number) + multiplicand_right_side)


def two_digit_number_string(times):
    """
    This function outputs a string with walls, spaces and a centred
    two-digit multiplier
    :param times: The multiplier
    """
    # Subtracts 12 from the width to centre the multiplier from the left side
    multiplicand_left_side = "#" + " " * int(width - 12)
    # Prints 8 empty strings to centre the multiplier from the right side
    multiplicand_right_side = " " * int(width - 12) + "#"
    print(multiplicand_left_side + str(times) + multiplicand_right_side)


def multiplication_string(number, times):
    """
    This function multiplies the two numbers together using repeated
    addition
    :param number: The multiplicand
    :param times: The multiplier
    """
    # Defines addition_answer outside of loop so it the loop can increase addition_answer by the multiplicand each time
    addition_answer = 0
    for i in range(times):
        addition_answer = addition_answer + number
    print(" " + str(number) + " * " + str(times) + " = " + str(addition_answer))


def top_rectangle(number):
    """
    This function calls other functions to create the top rectangle
    of the grid
    :param number: The multiplier
    """
    block_string()
    outline_string()
    four_digit_number_string(number)
    outline_string()
    block_string()


def bottom_rectangle(times):
    """
    This function call other functions to create the bottom rectangle
    of the grid
    :param times: The multiplier
    """
    block_string()
    outline_string()
    two_digit_number_string(times)
    outline_string()
    block_string()


def grid(number, times):
    """
    This function uses other functions above to output the final grid
    (i.e., both rectangles and the results of the multiplication)
    :param number: The multiplicand
    :param times: The multiplier
    """
    top_rectangle(number)
    multiplication_string(number, times)
    bottom_rectangle(times)


main()
