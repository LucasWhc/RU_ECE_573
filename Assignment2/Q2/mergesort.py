# The design concept of my codes are original from the course slides
def merge_sort(input_list):

    if len(input_list) == 1:
        return input_list, 0
    else:
        left_list, cnt_left = merge_sort(input_list[:len(input_list) // 2])
        right_list, cnt_right = merge_sort((input_list[len(input_list) // 2:]))

        cnt_comparison = 0 + cnt_left + cnt_right
        left_pos, right_pos = 0, 0
        final_list = []

        while left_pos < len(left_list) and right_pos < len(right_list):
            if left_list[left_pos] < right_list[right_pos]:
                final_list.append(left_list[left_pos])
                left_pos += 1
            else:
                final_list.append(right_list[right_pos])
                right_pos += 1
                cnt_comparison += len(left_list) - left_pos

        final_list += left_list[left_pos:]

        final_list += right_list[right_pos:]

        return final_list, cnt_comparison
