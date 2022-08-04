def DeleteEnd(arr):
    if(len(arr)==0):
        print("No elements found.")
    else:
        del(arr[-1])
    print(arr)

DeleteEnd([1,2,3,4,5])