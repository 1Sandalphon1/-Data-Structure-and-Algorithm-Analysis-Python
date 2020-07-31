import random
import copy

#冒泡排序
def bubbleSort(arr):
    if not arr or len(arr)==1:
        return arr
    end=len(arr)-1
    while(end>0):
        for i in range(0,end):
            if(arr[i]>arr[i+1]):
                swap(arr,i)
        end-=1
    return arr


#插入排序
def insertSort(arr):
    if not arr or len(arr)<2:
        return arr
    for i in range(1,len(arr)):
        j=i-1
        while(j>=0 and arr[j]>arr[j+1]):
            swap(arr,j)
            j-=1
    return arr


#归并排序
def mergeSort(arr):
    length=len(arr)
    if(length==0 or length==1):
        return
    mergeProcess(arr,0,length-1)
def mergeProcess(arr,L,R):
    if (L==R):
        return
    mid=(L+R)//2
    mergeProcess(arr,L,mid)
    mergeProcess(arr,mid+1,R)
    merge(arr,L,mid,R)
def merge(arr,L,mid,R):
    #定义数组
    tmp=[0 for i in range(R-L+1)]
    p1,p2,i=L,mid+1,0
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



#对数器
def generateRandomArray(size,value):
    #生成长度随机的数组
    array=[]
    for i in range(size):
        array.append(random.randint(0,value)-random.randint(0,value))
    return array
def isEqual(arr1,arr2):
    #判断两个数组是否相等
    if(not arr1 and not arr2):
        return True
    elif((not arr1 and arr2 != []) or (not arr2 and arr1 != [])):
        return False
    elif(len(arr1) != len(arr2)):
        return False
    for i in range(len(arr1)):
        if(arr1[i]!=arr2[i]):
            return False
    return True
def detector():
    times=5000
    maxSize=10
    maxValue=100
    succeed=True
    for i in range(times):
        arr1=generateRandomArray(maxSize,maxValue)
        arr2=copy.copy(arr1)
        # arr1.sort()
        #一定正确的算法
        bubbleSort(arr1)
        #待续验证的算法
        insertSort(arr2)
        if(not isEqual(arr1,arr2)):
            succeed=False
            break
    if(succeed):
        print('Nice!')
    else:
        print('False!')


#交换函数
def swap(arr,i):
    tmp=arr[i]
    arr[i]=arr[i+1]
    arr[i+1]=tmp




if __name__ == '__main__':
    arr=[4,3,2,6,2,9,1,7]
    print(mergeSort(arr))
    print(arr)
    # detector()
