
def move_zeros(array):
    zeros = []
    zeros = [i for i in array if i == 0]
    
    array = [i for i in array if i != 0]


    ans = array + zeros
    
    return ans

# https://www.codewars.com/kata/52597aa56021e91c93000cb0