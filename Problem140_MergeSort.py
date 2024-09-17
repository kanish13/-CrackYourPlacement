
arr=[12, 11, 13, 5, 6]
def merge(num):
    if len(num)>1:
        mid=len(num)//2
        left=num[:mid]
        right=num[mid:]
        merge(left)
        merge(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                num[k]=left[i]
                i=i+1
                k=k+1
            else:
                num[k]=right[j]
                j=j+1
                k=k+1
        while i<len(left):
                num[k]=left[i]
                i=i+1
                k=k+1
        while j<len(right):
                num[k]=right[j]
                j=j+1
                k=k+1
merge(arr)
print(arr)
    
