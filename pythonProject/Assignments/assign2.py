# Student Number: 251214226
# Student Name: Jarry Wu

order_options = ["meal", "appetizer", "dessert", "beverages", "done"]  # Lists all order options in a list
meal_prices = [21.99, 10.99, 2.50]  # shows all meal prices for [pizza, calzone, vegan option premium] in a list
appetizer_prices = [4.99, 3.99]  # shows all appetizer prices for [cheese bread, garlic bread] in a list
dessert_prices = [4.59, 3.59]  # shows all dessert prices for [cinnamon sticks, cookies] in a list
beverage_prices = [2.50, 1.50]  # shows all beverage prices for [pop, bottled water] in a list
combo_discounts = [0.05, 0.15]  # shows combo discounts for [meal and drink combo, dinner combo] in a list
taxes_and_fees = [0.13, 3.99, 1.00]  # shows all taxes and fees for [tax, delivery fee, delivery surcharge] in a list


def discount(subtotal, discount_amount):
    """
    This function calculates the order subtotal after it has received a combo discount
    :param subtotal: The total of all orders before extra fees and taxes
    :param discount_amount: The discounted amount (in dollars) to apply to the subtotal
    :return: Discounted total as a float
    """
    discounted_amount = subtotal * discount_amount
    subtotal = subtotal - discounted_amount
    return subtotal


def delivery_distance_premium(customer_distance):
    """
    This function calculates the delivery charge based on the customer's distance from
    Happytime Pizza
    :param customer_distance: Input amount from customer to determine distance from store
    :return: The delivery charge (in dollars) or None (if more than 29km away)
    """
    if customer_distance < 10:
        return 0
    elif 10 <= customer_distance <= 19:
        distance_fee = taxes_and_fees[2] * 2
        return distance_fee
    elif 20 <= customer_distance <= 29:
        distance_fee = taxes_and_fees[2] * 4
        return distance_fee
    else:
        return None


def tip(subtotal, tip_percentage):
    """
    This function calculates a tip amount (in dollars) based on the order subtotal and the
    customer's chosen tip percentage
    :param subtotal: The total of all orders before extra fees and taxes
    :param tip_percentage: Input amount from customer
    :return: The tip amount in dollars as a float
    """
    tip_amount = subtotal * (tip_percentage/100)
    return tip_amount


def tax(subtotal):
    """
    This function calculates the total amount of tax to be added to the order (in dollars)
    :param subtotal: The total of all orders before extra fees and taxes
    :return: The tax amount in dollars as a float
    """
    tax_amount = subtotal * taxes_and_fees[0]
    return tax_amount


def is_valid_option(customer_order_choice):
    """
    This function determines if the user has entered a valid choice from the Happytime Pizza
    menu options
    :param customer_order_choice: Input from customer can be meal, appetizer, dessert, done
    :return: True if the customer's input is valid; False if it is invalid
    """
    if customer_order_choice in order_options:
        return True
    return False


def customer_order():
    """
    This function calculates a subtotal based on the user's order choices
    :return: The subtotal calculated from all user choices as a float
    """
    subtotal = 0  # defines subtotal outside of loop, so it can accumulate with each order
    order_loops = False  # if order_loop is False and customer inputs "done" it will exit, otherwise it will continue
    meal_order_state = False  # boolean value used to track when a meal has been ordered
    appetizer_order_state = False  # boolean value used to track when an appetizer has been ordered
    dessert_order_state = False  # boolean value used to track when a dessert has been ordered
    beverages_order_state = False  # boolean value used to track when a beverage has been ordered
    order_state = True  # boolean value used to track when an order is finished
    while order_state is True:
        quantity = 0  # used to track how the quantity of a menu item ordered
        vegan_quantity = 0  # used to track how many of the meals ordered are vegan
        customer_order_choice = input("What would you like to order? OPTIONS: meal, appetizer, dessert, beverages \n").lower()
        if is_valid_option(customer_order_choice) is False:
            print("Sorry, but that option is not recognized.\n\nPlease try again.\n")
            customer_order_choice = customer_order_choice
        if customer_order_choice == "meal":
            meal_order = input("What meal would you like to order? OPTIONS: pizza, calzone\n")
            if meal_order == "pizza":
                pizza_quantity = int(input("How many pizzas would you like?\n"))
                subtotal = subtotal + pizza_quantity * meal_prices[0]
                while pizza_quantity > 0:
                    quantity = quantity + 1  # used to ask if each quantity of pizza should be vegan
                    pizza_vegan = input("Is pizza #" + str(quantity) + " vegan? y/n\n")
                    pizza_quantity = pizza_quantity - 1  # reduces quantity by 1 so while loop exist on last pizza
                    if pizza_vegan == "y":
                        vegan_quantity = vegan_quantity + 1  # increases by 1 everytime a vegan option is chosen
                subtotal = subtotal + vegan_quantity * meal_prices[2]
            else:
                calzone_quantity = int(input("How many calzones would you like?\n"))
                subtotal = subtotal + calzone_quantity * meal_prices[1]
                while calzone_quantity > 0:
                    quantity = quantity + 1  # used to ask if each quantity of calzone should be vegan
                    calzone_vegan = input("Is calzone #" + str(quantity) + " vegan? y/n\n")
                    calzone_quantity = calzone_quantity - 1  # reduces quantity by 1 so while loop exist on last calzone
                    if calzone_vegan == "y":
                        vegan_quantity = vegan_quantity + 1  # increases by 1 everytime a vegan option is chosen
                subtotal = subtotal + vegan_quantity * meal_prices[2]
            meal_order_state = True  # states that a meal has been ordered

        elif customer_order_choice == "appetizer":
            appetizer_order = input("What appetizer would you like to order? OPTIONS: cheese bread, garlic bread\n")
            if appetizer_order == "cheese bread":
                cheese_bread_quantity = int(input("How much cheese bread would you like?\n"))
                subtotal = subtotal + cheese_bread_quantity * appetizer_prices[0]
            else:
                garlic_bread_quantity = int(input("How much garlic bread would you like?\n"))
                subtotal = subtotal + garlic_bread_quantity * appetizer_prices[1]
            appetizer_order_state = True  # states that an appetizer has been ordered

        elif customer_order_choice == "dessert":
            dessert_order = input("What dessert would you like to order? OPTIONS: cinnamon sticks, cookies\n")
            if dessert_order == "cinnamon sticks":
                cinnamon_sticks_quantity = int(input("How many cinnamon sticks would you like?\n"))
                subtotal = subtotal + cinnamon_sticks_quantity * dessert_prices[0]
            else:
                cookies_quantity = int(input("How many cookies would you like?\n"))
                subtotal = subtotal + cookies_quantity * dessert_prices[1]
            dessert_order_state = True  # states that a dessert has been ordered

        elif customer_order_choice == "beverages":
            beverages_order = input("What beverage would you like to order? OPTIONS: pop, bottled water\n")
            if beverages_order == "pop":
                pop_quantity = int(input("How much pop would you like?\n"))
                subtotal = subtotal + pop_quantity * beverage_prices[0]
            else:
                bottled_water_quantity = int(input("How much bottled water would you like?\n"))
                subtotal = subtotal + bottled_water_quantity * beverage_prices[1]
            beverages_order_state = True  # states that a beverage has been ordered

        elif customer_order_choice == "done":
            if order_loops is False:
                print("Please try again later.")
                exit()
            else:
                order_state = False  # sets order_state to false so a "done" input continues to next code

        else:
            return customer_order()  # stops code from moving to next if statement is an invalid input is made

        if order_state is True:
            continue_order = input("Would you like to order another item? y/n\n")
            if continue_order == "n":
                order_state = False  # used to exit while loop
            else:
                order_loops = True  # sets order_loops to False so "done" no longer exits code

    if meal_order_state is True and appetizer_order_state is True and dessert_order_state is True and beverages_order_state is True:  # checks if all orders are fulfilled and then applies dinner combo discount
        discount_subtotal = round(subtotal * (1 - combo_discounts[1]), 2)  # calculates the discounted subtotal
        print("You ordered a meal, appetizer, dessert, and beverage. Please enjoy your 15% discount!")
        print("Your subtotal prior to the discount was: " + str(subtotal))
        print("Your new subtotal after the discount is: " + str(round(discount_subtotal, 2)))
        return discount_subtotal

    elif meal_order_state is True and beverages_order_state is True:  # checks if meal and drink combo is satisfied and then applies discount
        discount_subtotal = round(subtotal * (1 - combo_discounts[0]), 2)  # calculates the discounted subtotal
        print("You ordered a meal and beverage. Please enjoy your 5% discount!")
        print("Your subtotal prior to the discount was: " + str(subtotal))
        print("Your new subtotal after the discount is: " + str(round(discount_subtotal, 2)))
        return discount_subtotal
    else:
        return subtotal


def main():
    """
    This function asks the customer how far they are from the restaurant
    """
    delivery_charge = 0
    print("Thanks for visiting Happytime Pizza!\n")
    print("Please note: there is a fuel surcharge for longer trips.")
    delivery_distance = int(input("How many kilometres are you from the restaurant?\n"))
    if delivery_distance < 30:
        if delivery_distance < 10:  # if delivery distance is under 10km no distance premium is applied
            delivery_charge = taxes_and_fees[1]
        else:  # delivery charge + delivery premium for all distances above 10km
            delivery_charge = taxes_and_fees[1] + delivery_distance_premium(delivery_distance)
        print("The delivery charge for your order will be " + str(delivery_charge))
        continue_delivery = input("Would you still like to place an order with Happytime Pizza? y/n\n")
        if continue_delivery == "n":
            print("We understand. Have a good day!")
            exit()
    else:  # if delivery distance is over 30km, exit code
        print("Sorry, but we don't deliver that far away. Please visit us to enjoy our pizza and arcade.")
        exit()

    final_delivery_charge = round(delivery_charge, 2)  # rounds delivery fee to 2 decimal places
    final_subtotal = round(customer_order(), 2)  # calls customer_order() and rounds to 2 decimal places
    final_tax = round(tax(final_subtotal), 2)  # calculates tax relative to final subtotal
    final_tip = round(tip(final_subtotal, int(input("Please enter a tip percentage for the driver:\n"))), 2)  # takes final subtotal and calculates tip relative to subtotal
    final_charge = round(final_subtotal + final_tax + final_tip + final_delivery_charge, 2)  # calculates the final cost after all fees and taxes are added

    print("SUBTOTAL:" + f'{final_subtotal:>7.2f}')
    print("TAX:" + f'{final_tax:>12.2f}')
    print("TIP:" + f'{final_tip:>12.2f}')
    print("DELIVERY:" + f'{final_delivery_charge:>7.2f}')
    print("TOTAL:" + f'{final_charge:>10.2f}')


main()
