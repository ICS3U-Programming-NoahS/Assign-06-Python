#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Dec 18th, 2023
# This program asks you to enter 2 lists of different elements.
# The program will then display the two lists joined together
# and the two lists joined together with alternating elements.


def join_list(first_list, second_list):
    # join the two lists and and return new list
    return first_list + second_list


def alternate_list(first_list, second_list):
    # create empty list
    alternated_list = []

    # Initialize size of list
    size_of_list = len(first_list)

    # Use for loop to alternate elements of the 2 lists
    for counter in range(0, size_of_list):
        alternated_list.append(first_list[counter])
        alternated_list.append(second_list[counter])

    # Return alternated list
    return alternated_list


def main():
    # Greeting and instructions
    print("")
    print("This program asks you to enter 2 lists of different elements.")
    print("The program will then display the two lists joined together")
    print("and the two lists joined together with alternating elements:")
    print("(A, 1, B, 2, C, 3)")
    print("(A, B, C, 1, 2, 3)")
    print("")
    print("To end a list type in 'end'.")
    print("")

    # Create empty lists
    list_1 = []
    list_2 = []

    # Get list 1 elements using while true
    while True:
        list_1_element = input("Enter a list element for the first list: ")

        # Break if "end" is entered
        if list_1_element.lower() == "end":
            break
        else:
            list_1.append(list_1_element)

    # Get list 2 elements
    while True:
        list_2_element = input("Enter a list element for the second list: ")

        # Break if "end" is entered
        if list_2_element.lower() == "end":
            break
        else:
            # Add element to end of list
            list_2.append(list_2_element)

    # Calling the functions
    joined_list = join_list(list_1, list_2)
    alternated_list = alternate_list(list_1, list_2)

    # Display the lists
    print("")
    print("The lists joined:")
    print("{}".format(joined_list))
    print("")
    print("The lists alternated:")
    print("{}".format(alternated_list))


if __name__ == "__main__":
    main()
