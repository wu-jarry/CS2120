## TUTORIAL #4
## Jarry Wu

'''
The purpose of this file is to allow you to answer the questions from the tutorial
as comments, and then to write the code that must be submitted.

When you submit on Gradescope, all that is checked is the code portion of the tutorial,
so you don't have to answer the pre-tutorial questions here if you don't want to.

For the code questions, Gradescope will run an autograder. If you pass all the tests,
you can assume that you will get full marks on the tutorial. If you don't pass the tests,
you can resubmit as often as you would like up until the deadline.
'''

'''
Pre-Tutorial Questions

1. 

'''

'''
Demonstration

If you wish, you can write down the code that the TA uses in the tutorial to use later.
As long as it is between the triple apostrophes, it will be ignored by the Python 
interpreter. If you wish to run it, then just remove the triple apostrophes, BUT remember
to put them back before you submit, or the autograder may not work properly.


'''

# TUTORIAL TASK
######################### INSERT YOUR CODE BELOW #########################
# QUESTION #1 - DEFINE THE is_multiple() FUNCTION


def is_multiple(number_multiple):
    if number_multiple % 9 == 0 or number_multiple % 5 == 0:
        return True
    return False


# QUESTION #2 - DEFINE THE is_between() FUNCTION


def is_between(number_between):
    if number_between * 10 < 100 and number_between - 8 > 0:
        return True
    return False


# QUESTION #3 - DEFINE the count() FUNCTION


def count(number_count):
    if number_count > 30:
        print(number_count)
        print(str(number_count) + " is too large. Stop counting!")
        return
    else:
        print(number_count)
    count(number_count + 1)
# QUESTION #4 - DEFINE THE main() FUNCTION


def main(name, number_main):
    if is_multiple(number_main) is True and is_between(number_main) is True:
        print(str(name) + " chose a number that makes both functions evaluate as True")
    elif is_multiple(number_main) is True or is_between(number_main) is True:
        print(str(name) + " chose a number that makes one of the functions evaluate as True")
    else:
        print(str(name) + " chose a number that makes both functions evaluate as False")
    count(number_main)


main(str(input("What is your name? \n")), int(input("What is your favourite number? \n")))
######################### INSERT YOUR CODE ABOVE #########################