# import cmath


def addition(nums):
    nums = nums.replace(",", ".")
    nums = nums.split()
    natural = chek_natural(nums)
    imagine = chek_imagine(nums)
    natural_score = addition_natural(natural)
    imagine_score = addition_imagine(imagine)

    if len(imagine) == 0:
        result = natural_score
    elif len(natural) == 0:
        result = imagine_score
    else:
        result = 0

    return result


def addition_natural(nums):
    result = float(0)
    for i in range(0, len(nums)):
        result = result + float(nums[i])
    return result


def addition_imagine(nums):
    result = nums
    return result


def chek_natural(nums):
    natural = []
    point = "."
    for i in range(0, len(nums)):
        temp = str(nums[i])
        if point in temp or temp.isdigit():
            natural.append(temp)
    return natural


def chek_imagine(nums):
    imagine = []
    point = "."
    for i in range(0, len(nums)):
        temp = str(nums[i])
        if point in temp or temp.isdigit():
            temp = temp
        else:
            imagine.append(temp)
    return imagine