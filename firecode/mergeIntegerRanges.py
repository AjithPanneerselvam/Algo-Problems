def merge_ranges(input_range_list):
    if (input_range_list == None or len(input_range_list) <= 1):
        return input_range_list
    output_list = []
    previous = input_range_list[0]
    i = 1
    while i < len(input_range_list):
        current = input_range_list[i]
        if (previous.upper_bound >= current.lower_bound):
            merged = Range(previous.lower_bound, max(previous.upper_bound, current.upper_bound));
            previous = merged
        else:
            output_list.append(previous)
            previous = current
        i = i + 1

    output_list.append(previous)
    return output_list
