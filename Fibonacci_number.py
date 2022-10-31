import sys
sys.set_int_max_str_digits(10**6)


def fib(n):
    if n<10:
        return [1,1,2,3,5,8,13,21,34,55][n]
    elif n % 2==0:
        return fib(n//2)**2+fib(n//2-1)**2
    else:
        return fib(n//2)(fib(n//2+1)+fib(n//2-1))


n = int(input())
print(fib(n))
