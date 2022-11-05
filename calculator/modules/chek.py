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
            continue
        else:
            imagine.append(temp)
    return imagine