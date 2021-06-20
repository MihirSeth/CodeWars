import re
def order(sentence):
    if sentence == '':
        return ''
    newList = sentence.split()
    numbers = {
        '1':'',
        '2':'',
        '3':'',
        '4':'',
        '5':'',
        '6':'',
        '7':'',
        '8':'',
        '9':''
    }
    for i in newList:
        num = re.findall(r'\d', i)
        num = num[0]
        numbers[num] = i
        
    vals = []
    for i in numbers.values():
        if i =='':
            pass
        else:
            vals.append(i)
    
    joined = ' '.join(vals)
    return joined

order("is2 Thi1s T4est 3a")
# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python