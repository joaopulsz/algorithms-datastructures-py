def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                item = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = item
    return my_list


def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        minimum_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[minimum_index]:
                minimum_index = j
        if i != minimum_index:
            item = my_list[i]
            my_list[i] = my_list[minimum_index]
            my_list[minimum_index] = item
    return my_list


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        item = my_list[i]
        j = i - 1
        while item < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = item
            j -= 1
    return my_list


def merge(list1, list2):  # helper func for the following sort algorithm
    combined_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined_list.append(list1[i])
            i += 1
        else:
            combined_list.append(list2[j])
            j += 1
    while i < len(list1):
        combined_list.append(list1[i])
        i += 1
    while j < len(list2):
        combined_list.append(list2[j])
        j += 1
    return combined_list


def merge_sort(my_list):  # recursively divides a list in half until there are striclty 1 item lists, and then sorts and reunites them
    if len(my_list) == 1:
        return my_list
    middle_index = int(len(my_list) / 2)
    first_half = merge_sort(my_list[:middle_index])
    second_half = merge_sort(my_list[middle_index:])
    return merge(first_half, second_half)


print(merge_sort([9, 1, 7, 3, 6, 5, 10, 8, 2, 4]))
