# The program will ask the user to input a number that they want to look for in a list
# The list will be randomly generated with a random range, where the range includes this number but the list
# will not necessarily include this number
# The list will be first sorted using Merge Sort (Von Neumann's Algorithm) and then we are going to use binary search
# to find the number in the list

from numpy import random as rd

N = 25
k = 2*N + 1


def main():
    print("Welcome to Merge-Sort-Binary-Search Program")
    num = input("Please input an integer: ")
    print("The program will generate a random list that might or might include this {}".format(num))
    print("Generating a list...Please Wait")
    gen_list = rd.choice(range(int(num)-k, int(num) + k), N, replace=False)
    gen_list = sort_(list(gen_list))
    if not binary_search(int(num), gen_list):
        print("We have not found {} in the random generated list".format(num))
        print("Here is the random generated list")
        print(gen_list)
        return print("Have a wonderful rest of your day!")
    else:
        print("We have found {} in the random generated list".format(num))
        print("Here is the random generated list")
        print(gen_list)
        return print("Have a wonderful rest of your day!")


def sort_(num_list):
    """Sorts the list from least to greatest"""
    if len(num_list) <= 1:
        return num_list

    left = num_list[:int(len(num_list) / 2)]
    right = num_list[int(len(num_list) / 2):]

    left = sort_(left)
    right = sort_(right)

    return merge_(left, right)


def merge_(lst1, lst2):
    """Merges two sorted lists"""
    merged_list = []

    while lst1 != [] and lst2 != []:
        if lst1[0] <= lst2[0]:
            merged_list.append(lst1[0])
            lst1 = lst1[1:]
        else:
            merged_list.append(lst2[0])
            lst2 = lst2[1:]

    if not lst1:
        return merged_list + lst2

    else:

        return merged_list + lst1


def binary_search(n, lst):
    """Returns True is number is in the sorted list, otherwise outputs False"""
    if not lst:
        return False
    if n == lst[int(len(lst)/2)]:
        return True
    elif n < lst[int(len(lst)/2)]:
        return binary_search(n, lst[:int(len(lst)/2)])
    else:
        return binary_search(n, lst[int(len(lst)/2)+1:])


main()

