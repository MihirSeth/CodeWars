def tribonacci(signature, n):
    Tribonacci = 0
    x = signature[0]
    y = signature[1]
    z = signature[2]
    ans = []
    while Tribonacci<n and len(ans)<n:
        Tribonacci += 1
        calc = x+y+z
        hi = ans.append(x)
        x = y
        y = z
        z = calc     
    
    return ans

# https://www.codewars.com/kata/556deca17c58da83c00002db