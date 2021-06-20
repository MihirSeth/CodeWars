def spin_words(sentence):

    words = sentence.split()
    ans = []

    for i in words:
        if len(i)>= 5:
            ans.append(i[::-1])
        else:
            ans.append(i)
    
    return ' '.join(ans)



# https://www.codewars.com/kata/5264d2b162488dc400000001