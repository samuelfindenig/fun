def gridfinder(m, n, memo = {}):
    key = m, n
    if key in memo:
        return memo[key]
    elif m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    else:
        memo[key] = gridfinder(m-1, n) + gridfinder(m, n-1)
        return memo[key]


print(gridfinder(5,500))