## TUTORIAL #2
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

1. They capitalize constants

2. course_int = int('2120')

3. Whitespace

4. print(output_me)

5. 

6.

7.

8.

9.

'''

'''
Demonstration

If you wish, you can write down the code that the TA uses in the tutorial to use later.
As long as it is between the triple apostrophes, it will be ignored by the Python 
interpreter. If you wish to run it, then just remove the triple apostrophes, BUT remember
to put them back before you submit, or the autograder may not work properly.


'''

# TUTORIAL TASK
################ YOUR CODE GOES BELOW THIS LINE ###################

# QUESTIONS #1 and #2

def the_divider(first_number, second_number):
    print(first_number * second_number)
the_divider(2, 5)
the_divider(42390, 2304)



# QUESTIONS #3 to #5

def person_information(first_name='', last_name='', birth_year='', hometown=''):
    information = first_name + " " + last_name + ", " + str(birth_year) + ", " + hometown
    return(information)

print(person_information("Ada", "Lovelace", 1815, "London"))
print(person_information("John", "von Neumann", 1903, "Budapest"))
print(person_information("Grace", "Hopper", 1906, "New York City, NY"))
print(person_information("Claude", "Shannon", 1916, "Petoskey, MI"))
print(person_information("Tim", "Berners-Lee", 1955, "London"))

################ YOUR CODE GOES ABOVE THIS LINE ###################
