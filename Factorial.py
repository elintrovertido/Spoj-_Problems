import math
def zero(n):
    res = 0
    x = 5
    i = 1
    while x**i <= n:
        res += (n//(x**i))
        i = i + 1
    return res
if __name__ == "__main__":
    x = int(input())
    for i in range(x):
        n = int(input())
        print(zero(n))
# print(math.factorial(25))