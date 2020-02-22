# Part of my codes are original from the course slides and
# https://stackoverflow.com/questions/50912873/python-quicksort-with-median-of-three


def swap(input_list, pos1, pos2):
    input_list[pos1], input_list[pos2] = input_list[pos2], input_list[pos1]


def median_of_three(input_list, left, right):
    mid = (left + right - 1) // 2
    data1 = input_list[left]
    data2 = input_list[mid]
    data3 = input_list[right - 1]
    if data1 <= data2 <= data3 or data3 <= data2 <= data1:
        return data2, mid
    elif data1 <= data3 <= data2 or data2 <= data3 <= data1:
        return data3, right - 1
    else:
        return data1, left


def partition(input_list, left, right):
    pivot, index = median_of_three(input_list, left, right)
    swap(input_list, left, index)
    i = left + 1
    for j in range(left + 1, right):
        if input_list[j] < pivot:
            swap(input_list, i, j)
            i += 1
    swap(input_list, left, i - 1)
    return i - 1


def quick_sort(input_list, left, right):
    if left < right:
        index = partition(input_list, left, right)
        quick_sort(input_list, left, index)
        quick_sort(input_list, index + 1, right)


def quick_sort_cutoff(input_list, left, right, cutoff):
    if len(input_list) <= cutoff:
        for i in range(left + 1, right):
            for j in range(i, left, -1):
                if input_list[j] < input_list[j - 1]:
                    swap(input_list, j, j - 1)
                else:
                    break
        return
    if left < right:
        index = partition(input_list, left, right)
        quick_sort_cutoff(input_list, left, index, cutoff)
        quick_sort_cutoff(input_list, index + 1, right, cutoff)
