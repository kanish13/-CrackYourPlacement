arr=[12, 11, 13, 5, 6]
n=len(arr)
for i in range(1,n):
        j=i-1
        while j>-1:
            if arr[j]>arr[i]:
                arr[j],arr[i]=arr[i],arr[j]
                i=j
                j=j-1
            else:
                break
print(arr)
