from modules.chek import chek_natural
from modules.chek import chek_imagine


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
    answer = 0
    if len(nums) == 1:
        result = str(nums[0])
    else:
        for i in range(0, len(nums)):
            temp_new = list(nums[i])
            last_imagine_new = temp_new[len(temp_new) - 1]
            if last_imagine == last_imagine_new:
                del temp_new[len(temp_new) - 1]
                temp_new = ("".join(temp_new))
                answer = answer + int(temp_new)
                result = str(answer)+str(last_imagine_new)
            else:
                result = "Ошибка. Калькулятор не вычитает комплексные числа разных типов"
                break
    return result
