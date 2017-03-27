def fib(one, two, max, sum):
    if two % 2 == 0:
        sum += two
    if one + two >= max:
        return sum
    else:
        return fib(two, one + two, max, sum)

print(fib(1,2,4000000,0))