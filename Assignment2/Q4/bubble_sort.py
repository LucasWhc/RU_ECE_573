def bubble_sort(input_list):
    length = len(input_list)
    for i in range(length):
        for j in range(0, length - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
