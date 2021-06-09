from collections import Counter


def find_it(seq):
    hello = Counter(seq)

    vals = list(hello.keys())

    for i in vals:
        calc = hello[i]
        if calc%2 == 1:
        
            return i

# https://www.codewars.com/kata/54da5a58ea159efa38000836