def InsertStart(arr,length,value):
    if(len(arr)<length):
        arr.append(arr[-1])
        for i in range(length-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=value
        print(arr)
    else:
        print("Array is full")

if __name__=="__main__":
    InsertStart([1,2,3,4,5],6,0)