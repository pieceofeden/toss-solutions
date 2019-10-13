start = int(input(''))
end = int(input(''))
step = int(input(''))
def Range(start,end,step):
    while(start < end):
        print(start)
        start+=step
Range(start,end,step)