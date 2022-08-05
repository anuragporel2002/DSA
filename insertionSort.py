def InsertionSort(arr):
    if len(arr)>0:
        for i in range(1,len(arr)):
            key=arr[i]
            j=i-1
            while (j>=0 and key<arr[j]):
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        
    return arr

if __name__=="__main__":
    print("Sorted Array: ",InsertionSort([12,11,13,5,6]))