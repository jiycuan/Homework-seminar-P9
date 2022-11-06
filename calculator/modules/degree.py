from modules.chek import eazy_chek
def degree(nums):
    nums = nums.replace(",", ".")
    nums = nums.split()
    result = eazy_chek(nums[0])

    for i in range(1, len(nums)):
        temp = eazy_chek(nums[i])
        result = result/temp
    return result
