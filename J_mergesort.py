def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        first_half=arr[:mid]
        last_half=arr[mid:]

        mergesort(first_half)
        mergesort(last_half)

        i=j=k=0

        while(i<len(first_half) and j<len(last_half)):
            if first_half[i]<last_half[j]:
                arr[k]=first_half[i]
                i=i+1
            else:
                arr[k]=last_half[j]
                j=j+1
            k=k+1
        
        while(i<len(first_half)):
            arr[k]=first_half[i]
            k=k+1
            i=i+1
        
        while(j<len(last_half)):
            arr[k]=last_half[j]
            j=j+1
            k=k+1

mylist=[3,15,23,1]
mergesort(mylist)
print(mylist)