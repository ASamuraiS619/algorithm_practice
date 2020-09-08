def bubble_sort(number_list):
    flag = False
    while flag == False:
        flag = True
        length = len(number_list)
        times = 0
        for i in range(length - 1, times, -1):
            if number_list[i-1] > number_list[i]:
                flag = False
                number_list[i-1], number_list[i] = number_list[i], number_list[i-1]
        times += 1
    else:
        return number_list

print(bubble_sort([3, 5, 4, 6, 1, 2]))
