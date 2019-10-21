lst=list(map(int, input().split()))
lst=list(set(lst))
lst.sort()
print(lst[1]-lst[0])