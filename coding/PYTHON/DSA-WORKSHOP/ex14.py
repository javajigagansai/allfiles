def mergesort(arr):
    if len(arr)>1:
        a=len(arr)//2
        l=arr[:a]
        r = arr[:a]
        mergesort(l)
        mergesort(r)
        b=c=d=0
        while b<len(l) and c< len(r):
            if l[b] <r[c]:
                arr[d]=l[b]
                b+=1
            else:
                arr[d]=l[c]
                c+=1
                d+=1
def printlist(arr):
    for i in range(len(arr)):
        print(arr[i],end="")
    print()
if __name__=='__main__':
    arr=[0,1,3,5,7,9,2,4,6,8]
    mergesort(arr)
    print("sorted array is :")
    printlist(arr)
