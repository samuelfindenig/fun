def faktrorial(num):
    if num == 1:
        return num
    else:
        return num*faktrorial(num-1)
    

print(faktrorial(2))