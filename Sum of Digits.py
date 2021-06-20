def digital_root(number):
    number = str(number)

    first_recursion = []
    second_recursion = []
    third_recursion = []
    fourth_recursion = []


    for i in number:
        i = int(i)
        first_recursion.append(i)

    sum1 = sum(first_recursion)


    if sum1 >= 11:
        hi = str(sum1)

        for i in hi:
            i = int(i)

            second_recursion.append(i)

        
        sum2 = sum(second_recursion)
        
    
        if sum2 >= 11:
            hello = str(sum2)

            for i in hello:
                i = int(i)
                third_recursion.append(i)
            
            sum3 = sum(third_recursion)

            if sum3 >= 11:
                why = str(sum3)

                for i in why:
                    i = int(i)
                    fourth_recursion.append(i)
                
                sum4 = sum(fourth_recursion)
                return sum4

            else:
                if sum3 == 10:
                    return 1
                
                else:
                    return sum3
            
        
        else:
            if sum2 == 10:
                return 1
        
            else:
                return sum2


    else:
        if sum1 == 10:
            return 1
        
        else:
            return sum1



digital_root()

# https://www.codewars.com/kata/541c8630095125aba6000c00


