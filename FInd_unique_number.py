from collections import Counter
def find_uniq(arr):
    low_value = Counter(arr).most_common()[-1][0]
    return low_value  

# https://www.codewars.com/kata/585d7d5adb20cf33cb000235