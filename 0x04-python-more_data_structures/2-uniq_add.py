#!usr/bin/python3

def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_ints = set()

    # Loop through the list and add unique integers to the set
    for num in my_list:
        if isinstance(num, int):
            unique_ints.add(num)

    # Return the sum of the unique integers
    return sum(unique_ints)
