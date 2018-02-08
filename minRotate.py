# Complete the function below.

def minRotate(inscription):
    size = len(inscription)
    min = 10000
    index = -1
    for i in range(size):
        if ord(inscription[i]) < min:
            min = ord(inscription[i])
            index = i
        if ord(inscription[i]) == min:
            for j in range(1,size - 1):
                k = index + j
                l = i+j
                if k >= size:
                    k = k%size
                if l >= size:
                    l = l%size
                if ord(inscription[k]) == ord(inscription[l]):
                    pass
                elif ord(inscription[k]) < ord(inscription[l]):
                    break
                else:
                    index = i
                    break
    return index
