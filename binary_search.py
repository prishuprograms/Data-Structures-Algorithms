from util import time_it

@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return  mid_index
        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index -1

    return -1

@time_it
def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number == number_to_find:
        return mid_index
    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

def find_all_occurence(numbers_list, number_to_find):
    index = binary_search(numbers_list, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index - 1
    while i >= 0:
        if numbers_list[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i < len(numbers_list):
        if numbers_list[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)


if __name__ == '__main__':
    numbers_list = [1,4,6,11,67,67,67,17,21,67,34,67]
    # numbers_list.sort()
    number_to_find = 67

    # numbers_list = [i for i in range(100001)]
    # number_to_find = 100000

    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary_search ")

    index = linear_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using linear_search ")

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list) - 1)
    print(f"Number found at index {index} using binary_search_recursive ")

    indices = find_all_occurence(numbers_list, number_to_find)
    print(f"Indices of occurence of {number_to_find} are {indices}")
