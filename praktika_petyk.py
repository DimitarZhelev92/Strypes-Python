def numbers_to_msg(nums):
    chars = {0:'',
            1:'abc',
            2:'def',
            3:'ghi',
            4:'jkl',
            5:'mno',
            6:'pqrs',
            7:'tuv',
            8:'wxyz'}
    group = []
    temp_group = []

    for el in nums:
        if temp_group == []:
            temp_group.append(el)
        
        elif el in temp_group:
            temp_group.append(el)
        
        else:
            if el > 0:
                group.append(temp_group)
                temp_group = []
                temp_group.append(el)
            else:
                group.append(temp_group)
                temp_group = []
    group.append(temp_group)
    result = ''
    for sub_group in group:
        char_pos = len(sub_group) % len(chars[sub_group[0]]) -1
        result = result + chars[sub_group[0]][char_pos]
    return result

print(numbers_to_msg([2,3,3,3,5,3,3,3,7,1,6,6,6]))