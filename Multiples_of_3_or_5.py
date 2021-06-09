def solution(number):

    num = []

    numbers = int(number)

    for i in range(numbers):
        if (i % 3 == 0) or (i%5==0):
            num.append(i)


        elif (i % 3 == 0) and (i%5==0):
            continue

    
    total = sum(num)

    return total


# https://www.codewars.com/kata/514b92a657cdc65150000006