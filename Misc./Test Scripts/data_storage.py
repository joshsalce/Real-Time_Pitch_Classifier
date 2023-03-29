import time
import random

data_dict = {}

def storage_test(data):
    # Generate Some data (List of 5 values)
    rand_data = random.sample(range(1, 50), 5)
    # Generate a random value to serve as an event ID (range of 0-5)
    rand_int = random.randint(1, 3)

    # Check to see if event ID is a key in dictionary
    if str(rand_int) not in data.keys():
        # If not: Create new entry in dictionary with event ID as key, first create a list
            # Then add randomly generated data to list
        data[str(rand_int)] = [rand_data]
    else:
        # Else: Add the list of data to the list in the dictionary's entry for the key
        data[str(rand_int)].append(rand_data)
    print(data)
    return data

on = True
while on:
    data_dict = storage_test(data_dict)
    time.sleep(5.0)

    for i in data_dict.keys():
        #print(len(data_dict[i]))
        if len(data_dict[i]) == 4:
            column_average = [sum(sub_list) / len(sub_list) for sub_list in zip(*data_dict[i])]
            print(column_average)
            on = False
