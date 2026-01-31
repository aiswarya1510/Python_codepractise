def reverse(num):
    ans=""
    while(num>0):
        rev=num%10
        num=num//10
        ans=ans+str(rev)
    ans=int(ans)
    return ans

def reverse2(num):
    rev=0
    while(num>0):
        rem=num%10
        rev=(rev*10)+rem
        num=num//10
    return rev
        
print(reverse2(1234))
