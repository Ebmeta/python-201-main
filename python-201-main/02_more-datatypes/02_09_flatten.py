# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list=[]
# for i in starter_list:
#     flattened_list += i

# print(flattened_list)

def flatten_list(input_list, output_list=None):
    if output_list is None:
        output_list = []

    for item in input_list:
        if isinstance(item, list):
            flatten_list(item, output_list)
        else:
            output_list.append(item)

    return output_list

nested_list = [[1, 2, [3, 4]], [5, [6, 7]], 8, [9]]
flat_list = flatten_list(nested_list)
print(flat_list)
