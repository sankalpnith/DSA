# you are given a string. Remove the characters if it contains same character more than the target limit.
# Make sure that it does not contain the repeating charater even after removing first set
# ex for target to be 3 - aabbbcc becomes aacc
# and aabbbacc becomes cc and caabbbacc becomes ""

def convert(input_str, target_num):
    stack = []
    start_window_index = 0
    window_size = 1
    temp_input = input_str
    for index, char in enumerate(input_str):
        # print(stack)
        if index == 0:
            continue
        if char == input_str[index-1]:
            window_size += 1
        else:
            if window_size >= target_num:
                temp_input = temp_input[:start_window_index] + temp_input[index:]
            else:
                if stack:
                    stack_value = stack[-1].get(input_str[index-1])
                    if stack_value:
                        starting_index = stack_value[0]
                        count = stack_value[1]
                    else:
                        starting_index,count = 0,0
                    # print(stack_value, window_size)
                    if window_size + count >= target_num:
                        # print("here")
                        stack.pop()
                        # print(temp_input)
                        temp_input = temp_input[:starting_index] + temp_input[starting_index+count+1:index-window_size] + temp_input[index:]
                        # print(temp_input)
                        add_in_stack = False
                    else:
                        add_in_stack = True
                else:
                    add_in_stack = True
                if add_in_stack:
                    # print(input_str[index-1])
                    stack.append({input_str[index-1]: [start_window_index, window_size]})

            start_window_index = index
            window_size = 1
        if index == len(input_str) -1 and stack and stack[-1].get(char):
            print(stack)
            stack_value = stack[-1].get(char)
            if stack_value:
                starting_index = stack_value[0]
                count = stack_value[1]
            else:
                starting_index, count = 0, 0
            print(stack_value, window_size)
            if window_size + count >= target_num:
                # print("here")
                stack.pop()
                # print(temp_input)
                temp_input = temp_input[:starting_index]
                # print(temp_input)
    return temp_input

i = 'cccaabbbac'
target = 3
output = convert(i, target)
print(output)