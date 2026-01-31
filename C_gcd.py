def gcd(num1,num2):
    list1=[]
    list2=[]
    for i in range(1,num1+1):
        if num1%i==0:
            fact1=num1//i
            list1.append(fact1)

    for j in range(1,num2+1):
        if num2%j==0:
            fact2=num2//j
            list2.append(fact2)

    for i in list1:
        for j in list2:
            if i==j:
                break
        return i
    

def gcd2(num1,num2):
    gcd=0

    if num1>num2:
        small=num2
    else:
        small=num1
    for i in range(small,0,-1):
        if(num1%i==0 and num2%i==0):
            # gcd=i    for normal range since we need the last match
            return i
    # return gcd

        
print(gcd2(7,35))
    
# print(gcd(7,35))

