
def bubblesort(list1):
    n=len(list1)
    for i in range(n,0,-1):
        for j in range(0,i-1):
            if(list1[j]>list1[j+1]):
                # temp=list1[j]
                # list1[j]=list1[j+1]
                # list1[j+1]=temp
                list1[j], list1[j + 1] = list1[j + 1], list1[j]


    return list1

print(bubblesort([5, 3, 8, 4, 2]))
