def to_underscore(string):

    string = str(string)
    
    res = [string[0].lower()]
    for c in string[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)
     
    return ''.join(res)


# https://www.codewars.com/kata/529b418d533b76924600085d