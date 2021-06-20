def create_phone_number(n):

    

    num1 = str(n[0])
    num2 = str(n[1])
    num3 = str(n[2])
    numinbracs = [num1,num2,num3]
    nums = ''.join(numinbracs)
    num4 = str(n[3])
    num5 = str(n[4])
    num6 = str(n[5])
    secondRoundNums = [num4,num5,num6]
    join_nums = ''.join(secondRoundNums)
    num7 = str(n[6])
    num8 = str(n[7])
    num9 = str(n[8])
    num10 = str(n[9])
    thirdRoundNums = [num7,num8,num9,num10]
    join_nums1 = ''.join(thirdRoundNums)


    ans = '(' + nums + ') ' + join_nums + '-' + join_nums1

    return ans





create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])