if __name__ == '__main__':
    num=int(input())
    while(num!=1):
        if(num%2==0):
            print(num)
            num=int((num)**(1/2))
        else:
            print(num)
            num=int((num)**(3/2))
    print(1)