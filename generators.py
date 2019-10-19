lst = list(map(int, input().split()))
start = lst[0]
count = lst[1]
n = lst[2]
def generator(start,count,n):
    i=0;
    ans=[]
    ans.append(start)
    for i in range(1,count):
        ans.append(start*(n**i))
        i+=1
    for _ in ans:
        print(_, end=" ")
generator(start,count,n)
