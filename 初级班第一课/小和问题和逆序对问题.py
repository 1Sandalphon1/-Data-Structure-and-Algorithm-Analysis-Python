 #小和问题
def smallSum(arr):
    length=len(arr)
    return(mergeSort(arr,0,length-1))
def mergeSort(arr,L,R):
    if(L==R):
        return 0
    mid=(L+R)//2
    return(mergeSort(arr,L,mid)+\
        mergeSort(arr,mid+1,R)+\
        merge(arr,L,mid,R))
def merge(arr,L,mid,R):
    p1=L
    p2=mid+1
    i=0
    tmp=[0 for i in range(R-L+1)]
    res=0
    while(p1<=mid and p2<=R):
        if(arr[p1]<arr[p2]):
            res+=arr[p1]*(R-p2+1)
            p1+=1
        else:
            p2+=1
    p1=L
    p2=mid+1
    while(p1<=mid and p2<=R):
        if(arr[p1]<arr[p2]):
            tmp[i]=arr[p1]
            p1+=1
        else:
            tmp[i]=arr[p2]
            p2+=1
        i+=1
    while(p2<=R):
        tmp[i]=arr[p2]
        p2+=1
        i+=1
    while(p1<=mid):
        tmp[i]=arr[p1]
        p1+=1
        i+=1
    for i in range(len(tmp)):
        arr[L+i]=tmp[i]
        i+=1
    return res


 #逆序对问题


if __name__ == '__main__':
    arr=[1,3,4,2,5]
    print(smallSum(arr))