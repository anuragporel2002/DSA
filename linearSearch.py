def LinearSearch(arr,value):
    i=0
    while(i<len(arr)):
        if(arr[i]==value):
            print("{} found at index {}.".format(value,i))
            break
        i+=1  
    if(i==len(arr)):
        print("{} not found in the array.".format(value))

LinearSearch([1,2,3,4,5],2)