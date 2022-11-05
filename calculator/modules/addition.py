# from chek import chek_natural
# from chek import chek_imagine

def addition(nums):
    nums = nums.replace(",", ".")
    nums = nums.split()
    natural = chek_natural(nums)
    imagine = chek_imagine(nums)
    natural_score = addition_natural(natural)
    imagine_score = addition_imagine(imagine)

    if len(imagine) == 0:
        result = str(natural_score)
    elif len(natural) == 0:
        result = str(imagine_score)
    else:
        result = str(natural_score) + "+" + str(imagine_score)

    return result


def addition_natural(nums):
    result = float(nums[0])
    for i in range(1, len(nums)):
        result = result + float(nums[i])
    return result


def addition_imagine(nums):
    temp = list(nums[0])
    last_imagine = temp[len(temp) - 1]
    if len(nums) == 1:
        result = str(nums[0])
    else:
        for i in range(0, len(nums)):
            temp_new = list(nums[0])
            last_imagine_new = temp[len(temp) - 1]
            if last_imagine == last_imagine_new:
                del temp_new[len(temp) - 1]
                temp_new = ("".join(temp))
                answer = int(temp_new)


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
            continue
        else:
            imagine.append(temp)
    return imagine