
#基本示例，递归求数组最大值
def getMax(arr,L,R):
    if(L==R):
        return arr[L-1]
    mid=(L+R)//2
    maxLeft=getMax(arr,L,mid)
    maxRight=getMax(arr,mid+1,R)
    return max(maxLeft,maxRight)



if __name__ == '__main__':
    arr=[4,3,2,6,1,9,4]
    print(getMax(arr,1,7))
