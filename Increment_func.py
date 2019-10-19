start = int(input(''))
end = int(input(''))
step = int(input(''))
lst = []
def Range(start,end,step):
    while(start < end):
        lst.append(start)
        start+=step
    for item in lst:
        print(item, end=" ")
Range(start,end,step)
