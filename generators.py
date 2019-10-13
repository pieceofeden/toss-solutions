start = int(input(''))
end = int(input(''))
power = int(input(''))
def generator(start,end,power):
    while(start <= end):
        print(start**power)
        start+=1
generator(start,end,power)