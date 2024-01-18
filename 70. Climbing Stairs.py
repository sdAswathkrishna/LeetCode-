def climbStairs(n):
    a = 1
    b = 1
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
    return b
output = climbStairs(5)
print(output)