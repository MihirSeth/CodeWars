def duplicate_encode(word):
    character = []
    word = word.lower()
    for chars in word:
        if word.count(chars) ==1:
            character.append("(")
        
        else:
            character.append(")")
    
    ret = "".join(character)
    return ret

# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c