import sys
import time

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

def quick_sort(number_lists, length=None):
    sys.setrecursionlimit(1000000)

    if length is None:
        length = len(number_lists[0])
    next_lists = []
    for sequence in number_lists:
        if len(sequence) == 1:
            next_lists.append(sequence)
        else:
            threshold = sequence[-1]
            left_point = 0
            right_point = len(sequence) - 1

            flag = False
            while True:
                for left_index in range(left_point, len(sequence)):
                    if sequence[left_index] >= threshold:
                        left_point = left_index
                        break

                for right_index in range(right_point, -1, -1):
                    if left_point > right_index:
                        next_lists.append(sequence[:left_point])
                        next_lists.append(sequence[left_point:])
                        break
                    elif left_point == right_index:
                        right_index = left_point
                        sequence[left_point], sequence[-1] = sequence[-1], sequence[left_point]
                        if left_point != 0:
                            next_lists.append(sequence[:left_point])
                        next_lists.append(sequence[left_point:left_point + 1])
                        if left_point != len(sequence) - 1:
                            next_lists.append(sequence[left_point + 1:])
                        flag = True
                        break
                    elif sequence[right_index] < threshold:
                        right_point = right_index
                        sequence[left_point], sequence[right_point] = sequence[right_point], sequence[left_point]
                        break
                    else:
                        pass
                if flag == True:
                    break
    if len(number_lists) == length:
        return [number[0] for number in number_lists]
    else:
        return quick_sort(next_lists, length)

start = time.time()
bubble = bubble_sort(list(range(10 ** 4, 0, -1)))
time2 = time.time()
print("bubble sort: {}".format(bubble), "elapsed_time: {}sec".format(time2 - start))
quick = quick_sort([list(range(10 ** 4, 0, -1))])
time3 = time.time()
print("quick sort: {}".format(quick), "elapsed_time: {}sec".format(time3 - time2))
