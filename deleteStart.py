def DeleteStart(arr):
    if(len(arr)==0):
        print("No elements found.")
    else:
        for i in range(1,len(arr)):
            arr[i-1]=arr[i]
        del(arr[-1])
    print(arr)

if __name__=="__main__":
    DeleteStart([1,2,3,4,5])
