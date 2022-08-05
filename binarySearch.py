def BinarySearch(arr,value):
    low=0
    high=len(arr)-1
    while(low!=high):
        mid=(low+high+1)//2
        print(mid)
        if(value==arr[mid]):
            print("{} found at index {}.".format(value,mid))
            break
        elif(value>arr[mid]):
            low=mid+1
        else:
            high=mid-1
    if(low==high):
        print("{} not found in the array.".format(value))
if __name__=="__main__":
    BinarySearch([1,2,3,4,5,6],6)