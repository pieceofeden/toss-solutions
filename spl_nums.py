num = input('Enter number: ')
lst = []
for digit in num:
    lst.append(int(digit))
num = int(num)
flag=0
i=1
while(i<=num):
    total=0
    count = i
    for item in lst:
        total = total + item**i
        if(total%num==0):
            k=total/num
            print("Yes! This number is special")
            print(k)
            flag=1
            break
        else:
            i+=1
    if(flag==1):
        break
    else:
        count+=1
        i=count
if(flag==0):
    k=-1
    print("Nope, this isnt")
    print(k)
