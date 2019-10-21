lst = list(map(int, input().split()))
for item in lst:
    i=0
    for _ in lst:
        if(_%item==0):
            i+=1
        if(i==len(lst)):
            gcd=item
print(gcd)