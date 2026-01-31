def anagram(string1,string2):
    if (len(string1)!=len(string2)):
        return False
    stringa=sorted(string1)
    stringb=sorted(string2)
    
    if (stringa==stringb):
        return True
    return False
    
print(anagram("dff","bca"))


def anagram2(stringa,stringb):
    val= all(x==y for x,y in zip(stringa,stringb))     #generattor : (expression for item in iterable)
    return val
print(anagram2("vbcc","bvncv"))