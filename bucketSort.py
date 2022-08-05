import insertionSort as IS

def BucketSort(arr):
    buckets=[]
    nos_of_bucket=10

    for i in range(nos_of_bucket):
        buckets.append([])
    
    for i in arr:
        ind=int(i*nos_of_bucket)
        buckets[ind].append(i)

    for i in range(len(buckets)):
        buckets[i]=IS.InsertionSort(buckets[i])

    sorted_arr=[]
    for i in buckets:
        sorted_arr+=i

    print("Sorted Array: ",sorted_arr)

if __name__=="__main__":
    BucketSort([0.897, 0.565, 0.656,0.1234, 0.665, 0.3434])
    
    