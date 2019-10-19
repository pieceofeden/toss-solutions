Input = list(map(int, input().split()))
num = str(Input[0])
lst = []
for digit in num:
    lst.append(int(digit))
num = int(num)
total=0
i=Input[1]
for item in lst:
    total = total + item**i
    i+=1
if(total%num==0):
    k=int(total/num)
    print(k)
else:
    k=-1
    print(k)
