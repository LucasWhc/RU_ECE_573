def shellsort(datalist, h_list):
    len_data = len(datalist)
    cnt_inside_loop = 0  # Used to count the number of comparison inside loop
    cnt_loop = 0  # Used to count the number of loop
    # Part of these codes are original from the course slides
    for h in h_list:
        for i in range(h, len_data):
            temp = datalist[i]
            j = i
            cnt_loop += 1
            while j >= h and datalist[j - h] > temp:
                cnt_inside_loop += 1
                datalist[j] = datalist[j - h]
                j -= h
            datalist[j] = temp
    print("The amount of comparison with shell sort is ", cnt_inside_loop + cnt_loop)
