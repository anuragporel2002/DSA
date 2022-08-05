def DeleteEnd(arr):
    if(len(arr)==0):
        print("No elements found.")
    else:
        del(arr[-1])
    print(arr)

if __name__=="__main__":
    DeleteEnd([1,2,3,4,5])