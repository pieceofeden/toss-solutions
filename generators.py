start = int(input())
count = int(input())
n = int(input())
def generator(start,count,n):
    i=0;
    while(start<=count):
        print(n**i)
        i+=1
        start+=1
generator(start,count,n)
