from collections import Counter
def anagrams(word, words):
    
    char = Counter(word)
    characters = Counter(words)

    wors = []

    for i in words:
        calc = Counter(i)
        if calc == char:
            wors.append(i)
        
        if char != char:
            return False



    return wors


# https://www.codewars.com/kata/523a86aa4230ebb5420001e1