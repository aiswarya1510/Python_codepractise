'''
Write code to check if two strings match where one string contains wildcard characters
This problem checks if two strings match where one string contains wildcard characters. The wildcards are:

* for any sequence of characters (including an empty sequence).
? for exactly one character.
'''


def wildcard(word,wildcard):


    #check for ?
    if len(word)==len(wildcard):
        flag=False
        for i in range(0,len(wildcard)):
            if wildcard[i]=="?":
                continue
            if word[i]==wildcard[i]:
                flag=True
            else:
                flag=False
        return flag
# print(wildcard("hello","he?lo"))  

def wildcardstar(word,wildcard):
    a=0
    b=0
    astericktrack=0

    while(a<len(word)):
        if(word[a]==wildcard[b]):
            a=a+1
            b=b+1
        elif(wildcard[b]=="?"):
            a=a+1
            b=b+1
        elif(wildcard[b]=="*"):
            if(b<len(wildcard)-1):
                astericktrack=b
                b=b+1
            else:
                return True
        elif(word[a]!=wildcard[b]):
            if(wildcard[b-1]=="*" and a<len(word)-1):
                b=astericktrack
                b=b+1
                a=a+1
            else:
                return False
        else:
            return False
            
    if(b<len(wildcard)-1):
        if(wildcard[b]=="*"):
            return True
        else:
            return False
    return True

        
    


print(wildcardstar("abc","*?c"))
        


