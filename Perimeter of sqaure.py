def perimeter(n):
    x = 0
    y = 1
    Fibonacci = 0
    n = n+1
    ans = []
    while Fibonacci<=n:
        Fibonacci += 1
        z = x+y
        ans.append(x)
        x = y
        y = z

    Sum = sum(ans)
    ans = Sum*4

    return ans

# https://www.codewars.com/kata/559a28007caad2ac4e000083