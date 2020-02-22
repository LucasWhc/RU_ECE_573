# The design concept of my codes are original from the course slides
def merge_sort(input_list):

    if len(input_list) == 1:
        return input_list
    else:
        left_list = input_list[:len(input_list) // 2]
        right_list = input_list[len(input_list) // 2:]
        left_list = merge_sort(left_list)
        right_list = merge_sort(right_list)

        left_pos, right_pos, list_pos = 0, 0, 0

        while left_pos < len(left_list) and right_pos < len(right_list):
            if left_list[left_pos] < right_list[right_pos]:
                input_list[list_pos] = left_list[left_pos]
                left_pos += 1
            else:
                input_list[list_pos] = right_list[right_pos]
                right_pos += 1
            list_pos += 1

        while left_pos < len(left_list) and right_pos == len(right_list):
            input_list[list_pos] = left_list[left_pos]
            left_pos += 1
            list_pos += 1

        while right_pos < len(right_list) and left_pos == len(left_list):
            input_list[list_pos] = right_list[right_pos]
            right_pos += 1
            list_pos += 1

    return input_list
