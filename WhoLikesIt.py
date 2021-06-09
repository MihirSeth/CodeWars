def likes(names):

    length = len(names)-2
    length = str(length)

    if len(names) >= 4:
        name1 = names[0]
        name2 = names[1]       
        likes4 = name1 + ', ' + name2 + ' and ' + length + ' others like this'
        return likes4
    
    elif len(names) == 1:
        name1 = names[0]
        likes1 = name1 + ' likes this'
        return likes1
    
    elif len(names) == 2:
        name1 = names[0]
        name2 = names[1]

        likes2 = name1 + ' and ' + name2 + ' like this'
        return likes2
    
    elif len(names) == 3:
        name1 = names[0]
        name2 = names[1]
        name3 = names[2]
        likes3 = name1 + ', ' + name2 + ' and ' + name3 + ' like this'
        return likes3
    
    else: 
        noone = 'no one likes this'
        return noone

# https://www.codewars.com/kata/5266876b8f4bf2da9b000362