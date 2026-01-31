'''
1.  starts with 0,1


0,1,1,2,3,5,8,13
eg: num=4
0,1,1,2
'''
def Fibo(num):
    num1=0
    num2=1
    print(num1)
    print(num2)

    while(num-2>0):
        sum=num1+num2
        num1=num2
        num2=sum
        num=num-1
        print(sum)

    return ""
# Fibo(4)


def Fiborec(num):   # to find the nth fibonacci number
    if num<=0:
        return "Incorrect Number please add a positive number"
    elif num==1:
        print(0)
        return 0
    elif num==2:
        print(1)
        return 1
    else:

        total1=Fiborec(num-1)
        total2=Fiborec(num-2)
        return Fiborec(num-1)+Fiborec(num-2)
    
print(Fiborec(4))
    
