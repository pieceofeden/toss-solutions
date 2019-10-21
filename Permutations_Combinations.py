def factorial(num):
    fact=1
    while(num>0):
        fact=fact*num
        num-=1
    return fact
def permutation(n, r):
    per=(factorial(n)/factorial(n-r))
    return per
def combination(n, r):
    com=(factorial(n)/(factorial(r)*factorial(n-r)))
    return com

if __name__ == '__main__':
    a=int(input())
    b=int(input())
    print(permutation(a,b))
    print(combination(a,b))