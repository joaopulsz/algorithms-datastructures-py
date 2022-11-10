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


print(selection_sort([4, 6, 8, 11, 43, 1, 2, 5]))
