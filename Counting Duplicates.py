from collections import Counter
def duplicate_count(text):

    text = text.lower()
    
    dupcount = Counter(text)

    key = list(dupcount.keys())
    count = 0

    if text == '':
        return 0

    for i in key:
        calc = dupcount[i]
        if calc > 1:
            count = count+ 1
        
    
  
    return count




print(duplicate_count("Indivisibilities"))

# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1