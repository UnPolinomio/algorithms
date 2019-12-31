def merge(lst, low, high, mid_high):
    # Temporal copies of arrays
    temp_low = lst[low:mid_high]
    temp_high = lst[mid_high:high + 1]

    # Min index not checked of every temp array
    index_temp_low, index_temp_high = 0, 0

    # Index for be over-written in lst
    index_lst = low

    # Actual index of lst has min of temp lists
    while index_temp_low < len(temp_low) and index_temp_high < len(temp_high):

        if temp_low[index_temp_low] <= temp_high[index_temp_high]:
            lst[index_lst] = temp_low[index_temp_low]
            index_temp_low += 1
        else:
            lst[index_lst] = temp_high[index_temp_high]
            index_temp_high += 1

        index_lst += 1

    # When a temp list is all checked the other elements are already ordered
    while index_temp_low < len(temp_low):
        lst[index_lst] = temp_low[index_temp_low]
        index_lst += 1
        index_temp_low += 1

    while index_temp_high < len(temp_high):
        lst[index_lst] = temp_high[index_temp_high]
        index_lst += 1
        index_temp_high += 1
