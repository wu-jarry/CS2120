# Student Number: 251214226
# Student Name: Jarry Wu

import csv


def main():
    '''
    This function prompts the user to enter the name of a file that they would
    like to analyze.
    '''
    csv_file = input("Which file would you like to analyze?\n")
    try:
        with open(csv_file, "r") as reader_file:
            reader = csv.reader(reader_file)
            next(reader)
            #  Create a list of tuples with the vaccination date and vaccination total per date
            vaccines_doses_list = [(rows[0], int(rows[1])) for rows in reader]
            print(f'Total number of vaccinations: {vaccination_total(vaccines_doses_list)}')
            print(f'Median number of vaccinations: {median_number_vaccinations(vaccines_doses_list):.2f}')
            ranking_list = ["", "second ", "third "]
            for i in range(0, 3):  # Using a for loop to traverse the list of rankings when printing
                print(f'The week of {fewest_vaccinations(vaccines_doses_list)[i][0]} saw the {ranking_list[i]}fewest vaccinations: {fewest_vaccinations(vaccines_doses_list)[i][1]}')
            for i in range(0, 3):
                print(f'The week of {most_vaccinations(vaccines_doses_list)[i][0]} saw the {ranking_list[i]}most vaccinations: {most_vaccinations(vaccines_doses_list)[i][1]}')
            reader_file.close()
            with open("vaccination_data.txt", "w") as writer_file:
                writer_file.write(f'Total number of vaccinations: {vaccination_total(vaccines_doses_list)}\n')
                writer_file.write(f'Median number of vaccinations: {median_number_vaccinations(vaccines_doses_list):.2f}\n')
                for i in range(0, 3):  # Using a for loop to traverse the list of rankings when writing to file
                    writer_file.write(f'The week of {fewest_vaccinations(vaccines_doses_list)[i][0]} saw the {ranking_list[i]}fewest vaccinations: {fewest_vaccinations(vaccines_doses_list)[i][1]}\n')
                for i in range(0, 3):
                    writer_file.write(f'The week of {most_vaccinations(vaccines_doses_list)[i][0]} saw the {ranking_list[i]}most vaccinations: {most_vaccinations(vaccines_doses_list)[i][1]}\n')
                writer_file.close()
    except FileNotFoundError as err:  #  If the file doesn't exist run this piece of code and then end
        print(err)
        print(f'Sorry, but {csv_file} was not found.')
        print("The program will now end.")
        exit()


def fewest_vaccinations(doses_list):
    '''
    This function identifies the three days with the fewest vaccinations
    :param doses_list: The list containing the number of vaccinations by date
    :return: A tuple containing the three dates with the fewest
    vaccinations and the number of vaccinations on each of those dates
    '''
    fewest_vaccine_list = []
    doses_list.sort(key=lambda x: x[1])  # Using the second element in the tuple, sort the list from least to greatest
    for i in range(0, 3):
        fewest_vaccine_list.append(doses_list[i])  # Take the first 3 elements of the list after it's sorted
    return fewest_vaccine_list


def most_vaccinations(doses_list):
    '''
    This function identifies the three days with the most vaccinations
    :param doses_list: The list containing the number of vaccinations by date
    :return: A tuple containing the three dates with the most
    vaccinations and the number of vaccinations on each of those dates
    '''
    most_vaccine_list = []
    doses_list.sort(key=lambda x: x[1])   # Using the second element in the tuple, sort the list from least to greatest
    for i in range(-1, -4, -1):
        most_vaccine_list.append(doses_list[i])  # Take the last 3 elements of the list after it's sorted
    return most_vaccine_list


def median_number_vaccinations(doses_list):
    '''
    This function calculates the median number of vaccinations per day
    :param doses_list: The list containing the number of vaccinations by date
    :return: A floating-point value representing the median number of vaccinations per day
    '''
    median_vaccine_list = []
    doses_list.sort(key=lambda x: x[1])  # Using the second element in the tuple, sort the list from least to greatest
    for element in doses_list:
        median_vaccine_list.append(element[1])  # Append the vaccination totals per tuple into a new list
    median_vaccine_list.sort()
    if len(median_vaccine_list) % 2 == 0:  # Check to see if the vaccine list is even and find the median
        median_value = (median_vaccine_list[round(len(median_vaccine_list)//2)] + median_vaccine_list[round(len(median_vaccine_list)//2)+1])//2
        return float(median_value)
    return float(median_vaccine_list[len(median_vaccine_list)//2])  # Otherwise find the middle item in the list


def vaccination_total(doses_list):
    '''
    This function adds up the number of vaccine doses delivered by
    different locations on the same date to get a total number of
    vaccinations
    :param doses_list: The list containing the number of vaccinations by date
    :return: An integer containing the total number of vaccinations that took place
    '''
    sum_list = []
    for element in doses_list:  # Append the vaccination totals per tuple into a new list
        sum_list.append(element[1])
    return sum(sum_list)  # Find the sum of the new list to determine total vaccinations given


main()
