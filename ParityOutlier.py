def find_outlier(integers):

    # int_string = int(integers)
    even = []
    odd=[]

    for i in integers:
        if i%2 == 0:
            even.append(i)
        if i%2 == 1:
            odd.append(i)

    
    if len(even) == 1:
        return even[0]
    
    elif len(odd) == 1:
        return odd[0]




find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])