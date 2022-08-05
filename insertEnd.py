def InsertEnd(arr,length,value):
    if(len(arr)<length):
        arr.append(value)
        print(arr)
    else:
        print("Array is Full")

if __name__=="__main__":
    InsertEnd([1,2,3,4,5],6,6)