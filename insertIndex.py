def InsertAtIndex(arr,length,index,value):
    if(len(arr)<length):
        arr.append(arr[-1])
        for i in range(length-1,index,-1):
            arr[i]=arr[i-1]
        arr[index]=value
        print(arr)
    else:
        print("Array is full")

InsertAtIndex([1,2,3,4,5],6,2,9)