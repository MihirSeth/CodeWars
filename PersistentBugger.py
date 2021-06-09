def persistence(n):

    if n<10:
        return 0    
    num = str(n)
    total = 1
    for i in num:
        total = total * int(i)

    return 1 + persistence(total)

# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec