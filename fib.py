def fib(nun, memo = {}):
    if num in memo:
        return memo[num]
    elif num <= 2:
        return 1
    else:
        memo[num] = fib(num-1, memo)+fib(num-2, memo)
        return memo[num]
        
for i in range(1, 100):
    print(fib(i))