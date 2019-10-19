n = int(input())
if(1<=n<=100):
    lst =  list(map(int, input().split()))
    flag = 1
    for _ in lst:
        if(-100<=_<=100):
            count =  0
            for item in lst:
                if( _ == item):
                    count+=1
            if(count%2!=0):
                print(_)
                break
    if(count%2==0):
        print(-1)
