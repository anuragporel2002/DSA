def BubbleSort(arr):
    def Swap(n1,n2):
        n1=n1+n2
        n2=n1-n2
        n1= n1-n2
        return n1,n2
    for i in range(len(arr)):
        swapped=False
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=Swap(arr[j],arr[j+1])
                swapped=True
        if swapped==False:
            print("Sorted Array: ",arr)
            break

if __name__=="__main__":
    BubbleSort([5,3,1,4,8])