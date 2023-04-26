#YOUR NAME

my_list = ["Wanda,Maximoff,Scarlet Witch", "Stephen,Strange,Dr. Strange", "Steve,Rogers,Captain America",
           "Natasha,Romanoff,Black Widow", "Shang-Chi,Zheng,Master of Kung Fu", "Scott,Lang,Ant-Man",
           "T'Challa,,Black Panther"]
######################### INSERT YOUR CODE BELOW #########################
my_dict = {}
for element in my_list:
    identity = element.split(",")
    my_dict.update({identity[-1]: (identity[0], identity[1])})
print("\nThis is the dictionary:\n")
print(my_dict)

print("\nThese are the keys in the dictionary:\n")
for key, value in my_dict.items():
    print(key)

print("\nThese are the values in the dictionary:\n")
for key, value in my_dict.items():
    print(value)

print("\nThis is the truth:\n")
for key, value in sorted(my_dict.items()):
    if value[1]:
        print(f'{key} is really {value[0]} {value[1]}.')
    else:
        print(f'{key} is really {value[0]}.')

print(my_dict.keys())

######################### INSERT YOUR CODE ABOVE #########################