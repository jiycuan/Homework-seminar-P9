def chek_natural(nums):
    natural = []
    for i in range(0, len(nums)):
        temp = str(nums[i])
        if temp.replace('.', '').isdigit():
            natural.append(temp)
    return natural


def chek_imagine(nums):
    imagine = []
    for i in range(0, len(nums)):
        temp = str(nums[i])
        if temp.replace('.', '').isdigit():
            continue
        else:
            imagine.append(temp)
    return imagine


def eazy_chek(nums):
    if nums.replace('.', '').isdigit():
        result = float(nums)
    else:
        result = complex(nums)
    return result
