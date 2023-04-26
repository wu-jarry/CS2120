# Student Number: 251214226
# Student Name: Jarry Wu

import csv


def main():
    '''
    The function should read the file's contents into a dictionary
    of lists. Each list in the dictionary will be composed of tuples that
    represent Covid cases
    '''
    csv_file = input("Which file would you like to analyze?\n")
    try:
        with open(csv_file, "r") as reader_file:
            reader = csv.reader(reader_file)
            next(reader)
            vaccine_doses_dict = {}
            for rows in reader:
                if rows[0] not in vaccine_doses_dict:  # If the date doesn't exist, add it to the dictionary with the respective tuple
                    vaccine_doses_dict[rows[0]] = [tuple(rows[1:])]
                elif rows[0] in vaccine_doses_dict:  # If the date already exists, append the tuple to the list of values for that key
                    vaccine_doses_dict[rows[0]].append(tuple(rows[1:]))
            reader_file.close()
            total_count = 0
            for key, value in vaccine_doses_dict.items():
                for element in value:  # Finds the total MLHU cases recorded
                    total_count += 1
        with open("diagnosed_data.txt", "w") as writer_file:
            writer_file.write(f'There were {total_count} MLHU cases in total.\n')
            writer_file.write(f'Of those, there were {count_by_location(vaccine_doses_dict)[0]} cases reported in London.\n')
            writer_file.write(f'There were {count_by_location(vaccine_doses_dict)[1]} cases reported in Middlesex County.\n')
            writer_file.write(f'There were {count_by_location(vaccine_doses_dict)[2]} cases reported from an unknown location.\n\n')
            writer_file.write(f'Overall cases by age group:\n')
            writer_file.write(f'People under 40 accounted for {cases_by_age_group(vaccine_doses_dict)[0]} case(s).\n')
            writer_file.write(f'People between 40 and 80 accounted for {cases_by_age_group(vaccine_doses_dict)[1]} case(s)\n')
            writer_file.write(f'People over 80 accounted for {cases_by_age_group(vaccine_doses_dict)[2]} case(s).\n\n')
            writer_file.write(f'The most cases occurred on {peak_case_count(vaccine_doses_dict)[0]}.\n')
            writer_file.write(f'On that date, there were {sum(cases_by_age_by_date(peak_case_count(vaccine_doses_dict)[0], vaccine_doses_dict))} cases, broken down by age as follows:\n')
            writer_file.write(f'{cases_by_age_by_date(peak_case_count(vaccine_doses_dict)[0], vaccine_doses_dict)[0]} case(s) under 40.\n')
            writer_file.write(f'{cases_by_age_by_date(peak_case_count(vaccine_doses_dict)[0], vaccine_doses_dict)[1]} case(s) 40 to 80.\n')
            writer_file.write(f'{cases_by_age_by_date(peak_case_count(vaccine_doses_dict)[0], vaccine_doses_dict)[2]} case(s) over 80.\n')
            writer_file.close()
    except FileNotFoundError as err:  # If the file doesn't exist run this piece of code and then end
        print(err)
        print(f'Sorry, but {csv_file} was not found.')
        print("The program will now end.")
        exit()


def peak_case_count(doses_tuples):
    '''
    This function determines the day that had the peak number of cases
    :param doses_tuples: The dictionary containing lists of tuples representing cases
    :return: A tuple containing the date of the most cases and the number of cases that were handled on that date
    '''
    peak_count = 0
    peak_date = ""
    for key, value in doses_tuples.items():
        if len(value) > peak_count:
            peak_count = len(value)
            peak_date = key
    return peak_date, peak_count


def count_by_location(doses_tuples):
    '''
    This function determines the number of cases from each area the MLHU is responsible for
    :param doses_tuples: The dictionary containing lists of tuples representing cases
    :return: A tuple containing the counts for each of the three locations
    '''
    location_list = ["City of London", "Middlesex County", ""]
    london_counter = 0
    middlesex_counter = 0
    unknown_counter = 0
    for key, value in doses_tuples.items():
        for element in value:  # For every value in the dictionary, increase the counter if it is associated with the respective locations
            if element[2] == location_list[0]:
                london_counter += 1
            elif element[2] == location_list[1]:
                middlesex_counter += 1
            elif element[2] == location_list[2]:
                unknown_counter += 1
    return london_counter, middlesex_counter, unknown_counter


def cases_by_age_group(doses_tuples):
    '''
    This function counts the number of overall cases by each age group
    :param doses_tuples: The dictionary containing lists of tuples representing cases
    :return: A tuple with the counts for each age group
    '''
    under_40 = 0
    between_40_80 = 0
    above_80 = 0
    for key, value in doses_tuples.items():
        for element in value: # For every value in the dictionary, increase the counter if it is associated with the respective age
            if element[1] == "80+":
                above_80 += 1
            else:
                age_groups = element[1].split("-")
                if int(age_groups[-1]) < 40:
                    under_40 += 1
                else:
                    between_40_80 += 1
    return under_40, between_40_80, above_80


def cases_by_age_by_date(date, doses_tuples):
    '''
    This function counts the cases by age group (under 40, 40 to 80, over 80) for a given date
    :param date: The date for which we want information
    :param doses_tuples: The dictionary containing lists of tuples representing cases
    :return: A tuple with the counts for each age group
    '''
    under_40 = 0
    between_40_80 = 0
    above_80 = 0
    for key, value in doses_tuples.items():
        if key == date:  # Ensures that it's only counting the tuples for the given date
            for element in value: # For every value in the dictionary, increase the counter if it is associated with the respective locations
                if element[1] == "80+":
                    above_80 += 1
                else:
                    age_groups = element[1].split("-")
                    if int(age_groups[-1]) < 40:
                        under_40 += 1
                    else:
                        between_40_80 += 1
    return under_40, between_40_80, above_80


main()
