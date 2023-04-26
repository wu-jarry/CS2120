import turtle

######################### INSERT YOUR CODE BELOW #########################
# QUESTION #1 - ASK FOR USER INPUT
number = int(input("Please enter a number \n"))

# QUESTION #2 - CREATE A FUNCTION TO CHECK IF AN INTEGER IS EVEN


def is_even(number):
    number_state = number % 2
    if number_state == 0:
        print(str(number) + " is an even number \n")
    else:
        print(str(number) + " is an odd number \n")

# QUESTION #3 - CALL THE FUNCTION


is_even(number)

# QUESTION #4 - CREATE A TURTLE FUNCTION


def square(turtle_name, colour, side_length):
    steve = turtle.Turtle()
    steve.shape(turtle_name)
    steve.color(colour)
    for i in range(4):
        steve.forward(side_length)
        steve.left(90)
        print(steve.pos())
    print("")
    steve.hideturtle()


square("turtle", "blue", 50)

# QUESTION #5 - CREATE FOUR TURTLES
snap = turtle.Turtle()
crackle = turtle.Turtle()
pop = turtle.Turtle()
dave = turtle.Turtle()

snap.hideturtle()
crackle.hideturtle()
pop.hideturtle()
dave.hideturtle()


def turtle_square(turtle_name, colour, side_length):

    turtle_name.shape("turtle")
    turtle_name.showturtle()
    turtle_name.color(colour)
    for i in range(4):
        turtle_name.forward(side_length)
        turtle_name.left(90)
        print(turtle_name.pos())
    print("")
    turtle_name.hideturtle()


turtle_square(snap, "red", 100)
turtle_square(crackle, "orange", 200)
turtle_square(pop, "yellow", 300)
turtle_square(dave, "green", 400)

######################### INSERT YOUR CODE ABOVE #########################
# turtle.mainloop()  # keeps the image window open until you close it

