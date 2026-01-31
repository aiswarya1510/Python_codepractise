def perfectnum(num):
    total=0
    list1=[]
    for i in range(1,num):
        if(num%i==0):
            list1.append(i)

    for i in list1:
        total=i+total
    if total==num:
        return "perfect num"
    else:
        return "not a perfect num"
    
print(perfectnum(8))

def perfectnum2(num):
    total=0
    for i in range(1,num):
        if(num%i==0):
            total=total+i


    if total==num:
        return "perfect num"
    else:
        return "not a perfect num"
    
print(perfectnum2(28))

