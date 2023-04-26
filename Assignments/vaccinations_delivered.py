# Student Number: 251214226
# Student Name: Jarry Wu

import csv


def main():
    '''
    This function prompts the user to enter a .csv file to read
    The function should read the file's contents into a
    dictionary of lists. Each list in the dictionary contains the doses given at
    each location on a given date
    '''
    csv_file = input("Which file would you like to analyze?\n")
    try:
        with open(csv_file, "r") as reader_file:
            reader = csv.reader(reader_file)
            next(reader)
            #  Adds each row into a dictionary with the date as a key and the vaccine count per location as the value
            vaccine_doses_dict = {rows[0]: rows[1:] for rows in reader}
            reader_file.close()
            with open("vaccine_doses_by_date.csv", "w") as writer_file:
                writer_file.write("Date, Doses\n")
                #  Writes the date and total vaccine count on that day to a file
                for key, value in vaccine_doses_dict.items():
                    writer_file.write(f'{key}, ')
                    writer_file.write(f'{str(vaccinations_by_date(value))}\n')
            writer_file.close()
    except FileNotFoundError as err:  #  If the file doesn't exist run this piece of code and then end
        print(err)
        print(f'Sorry, but {csv_file} was not found.')
        print("The program will now end.")
        exit()
    except IndexError as err:  #  If the item trying to be accessed in the file is out of range run this piece of code and end
        print(err)
        print("Sorry, but you tried to access information that does not exist.")
        print("Are you sure you entered the correct filename?")
        print("The program will now end.")
        exit()


def vaccinations_by_date(date_location_vaccine_count_list):
    '''
    This function adds up the number of vaccine doses administered at
    the different locations on each date in order to arrive at a total
    number of vaccinations for that date
    :param date_location_vaccine_count_list: A list containing the dose number for each location on a given date
    :return: A total vaccination count for that date
    '''
    for element in range(0, len(date_location_vaccine_count_list)):
        #  Takes each item in the list and convert it into an integer
        date_location_vaccine_count_list[element] = int(date_location_vaccine_count_list[element])
    return sum(date_location_vaccine_count_list) #  Adds together all items in the list and returns a total vaccine count per date


main()
