def rankarray(numlist):
    numcopy=numlist
    numcopy=sorted(numcopy)
    ans=[]
    for num in numlist:
        indexval=numcopy.index(num)
        ans.append(indexval+1)

    return ans

print(rankarray([40, 10, 20, 30]))

