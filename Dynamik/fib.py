# fib mit rekrusion
def fib(num, memo = {}):
    if num in memo:
        return memo[num]
    elif num <= 2:
        return 1
    else:
        memo[num] = fib(num-1, memo)+fib(num-2, memo)
        return memo[num]
        
# fib iterativ
def Fib(num): 
    a, b = 0, 1
    for i in range(0, num):
        a, b = b, a + b
    return a


