def Palindrome(val):
    val2=val[::-1]
    if (val==val2):
        return True
    return False

print(Palindrome("madam"))


def Palindrome2(val):
    start=0
    end=len(val)-1
    while(start<=end):
        if(val[start]!=val[end]):
            return False
        start=start+1
        end=end-1
        
    return True

print(Palindrome2("madama"))