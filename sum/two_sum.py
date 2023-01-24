

# function
def find_sum(nums, target):
    list_ans = []
    for i in range(len(nums)):
        if target - nums[i] in nums[i:]:
            # print(i)
            list_ans.append(i)

    return list_ans


# test
nums = [7,11,15,2]
target = 9
print(find_sum(nums, target))

nums = [3,2,4]
target = 6
print(find_sum(nums, target))

nums = [3,3]
target = 6
print(find_sum(nums, target))
