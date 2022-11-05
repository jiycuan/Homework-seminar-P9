import cmath

def addition(nums):
    nums_tuple = nums.split()
    sum = 0
    tuple_or_not = ','
    if tuple_or_not in nums:

    for i in range(0, len(nums_tuple)):
        sum = sum + int(nums_tuple[i])
    print(sum)

addition('25,11 21 26')


