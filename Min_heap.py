a = [2,3,5,6,8,1,4]
def build_heap(arr):
    res = [a[0]]
    for i in range(1,len(arr)):
        index = i
        res.append(a[i])
        while index >=0 and ((index+1)//2) -1 >=0:
            if res[((index+1)//2) -1] > res[index]:
                res[((index+1)//2) -1], res[index] = res[index], res[((index+1)//2) -1]
                index = ((index+1)//2) -1
                
            else:
                break
    return res

def pop(arr):
    ans = arr[0]
    index = 0
    while index < len(arr):
        if index*2 +2 < len(arr) and arr[index*2 + 1] and arr[index*2 +2] :
            if arr[index*2 + 1] < arr[index*2 +2]:
                arr[index] = arr[index*2 + 1]
                arr[index*2 + 1] = None
                index = index*2 + 1
            else:
                arr[index] = arr[index*2 + 2]
                arr[index*2 + 2] = None
                index = index*2 + 2
        elif index*2 + 1 < len(arr) and arr[index*2 + 1]:
            arr[index] = arr[index*2 + 1]
            arr[index*2 + 1] = None
            index = index*2 + 1
        elif index*2 + 2 < len(arr) and arr[index*2 + 2]:
            arr[index] = arr[index*2 + 2]
            arr[index*2 + 2] = None
            index = index*2 + 2
        else:
            break
    arr = arr[1:]
    return ans

a = build_heap(a)
for _ in a:
    print(pop(a))
