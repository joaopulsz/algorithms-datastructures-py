def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                item = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = item
    return my_list


print(bubble_sort([4, 6, 8, 11, 43, 1, 2, 5]))
