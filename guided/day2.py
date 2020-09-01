# 1. write list comp to generate list [1,2,3,4,5]
# y = [num for num in range(1, 6)]
# print(y)

# 2 write list comp to generate cubes of numbers 0-9
# y = [num**3 for num in range(0, 10)]
# print(y)

# 3. convert items to upper case
# a = ['foo', 'bar', 'baz']
# y = [item.upper() for item in a]
# print(y)

# 4.
# x = [int(item) for item in input("enter comma-separated numbers: ").split(',')]
# y = [item for item in x if item % 2 == 0]
# print(y)


# 5. return the centered average of an aray of ints, i.e. the mean average of the values, except ignoring the largest and smallest values in the array (list)

"""
if list > 2 ?
find the min and max

"""


def centered_avg(nums):
    # print(nums)
    min_num = 0
    max_num = 0
    offset = 0
    nums.sort()
    # print(nums)

    if len(nums) > 2:
        min_num = nums[0]
        max_num = nums[len(nums)-1]
        offset = 2

    tot = sum(nums)
    # print(tot)
    tot = tot - min_num - max_num
    # print(tot)

    return tot // (len(nums) - offset)


print(centered_avg([7, 1, 2, 3, 4, 5, 1, 0]))  # 1,1,2,3,4,5
print(centered_avg([1]))  # 1,1,2,3,4,5
print(centered_avg([1, -4]))  # 1,1,2,3,4,5
print(centered_avg([1, -4, 3]))  # 1,1,2,3,4,5
