# The design concept of my codes are original from the course slides
def merge_sort(input_list):
    cnt_comparison = 0

    if len(input_list) == 1:
        return input_list, 0
    else:
        left_list = input_list[:len(input_list) // 2]
        right_list = input_list[len(input_list) // 2:]
        left_list, cnt_left = merge_sort(left_list)
        right_list, cnt_right = merge_sort(right_list)

        cnt_comparison += cnt_left + cnt_right

        left_pos, right_pos, list_pos = 0, 0, 0

        while left_pos < len(left_list) and right_pos < len(right_list):
            cnt_comparison += 1
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

    return input_list, cnt_comparison


def bottomup_merge(input_list):
    cnt_comparison = 0
    length = len(input_list)
    size = 1

    while size < length:
        size += size
        for index in range(0, length, size):
            left_list = input_list[index:(index + size // 2)]
            right_list = input_list[(index + size // 2):(index + size)]
            temp = []
            left_pos, right_pos = 0, 0
            for temp_pos in range(0, size):
                if left_pos == len(left_list):
                    temp.append(right_list[right_pos])
                    right_pos += 1
                elif right_pos == len(right_list):
                    temp.append(left_list[left_pos])
                    left_pos += 1
                elif right_list[right_pos] < left_list[left_pos]:
                    cnt_comparison += 1
                    temp.append(right_list[right_pos])
                    right_pos += 1
                else:
                    cnt_comparison += 1
                    temp.append(left_list[left_pos])
                    left_pos += 1
            input_list[index:index + size] = temp
    return input_list, cnt_comparison
