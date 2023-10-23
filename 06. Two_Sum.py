# Given an array of integers nums and an integer target, return indices of the two numbers such that 
# they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

def two_nums (input_list, input_target):
    result_list = []
    x = 0
    while (x <= len(input_list)-1) and (len(result_list) == 0):
        y = 0
        while (y <= len(input_list)-1) and (len(result_list) == 0):
            if x != y:
                # print (f'y: {y}')
                # print (f'x: {x}')
                if (input_list[x] + input_list[y]) == input_target:
                    result_list.append(x)
                    result_list.append(y)
            y+=1
        x+=1
    return result_list

# nums = [2,7,11,15]
# target = 9

nums = [3,2,4]
target = 6

# nums = [3,3,7]
# target = 6

print (f'List: {nums})')
print (f'Target: {target}')
print (f"Result: {two_nums(nums, target)}\n")