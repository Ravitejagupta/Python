# Complete the function below.
def alert(inputs, windowSize, allowedIncrease):
    if len(inputs) == 0 or windowSize <= 0 or allowedIncrease <= 0:
        return True
    if len(inputs) <= windowSize:
        return False
    d = {}
    
    avg = sum(inputs[:windowSize])/windowSize
    for i in range(len(inputs) - windowSize + 1):
        if i!=0 and sum(inputs[i:i+windowSize])/windowSize > allowedIncrease * avg:
            return True
        else:
            avg = sum(inputs[i:i + windowSize]) / windowSize
        for j in inputs[i:i+windowSize]:
            if j > avg * allowedIncrease:
                if j in d:
                    d[j] +=1
                else:
                    d[j] = 1
    print(d)
    for k in d:
        if inputs.index(k) < windowSize - 1:
            if d[k] == inputs.index(k) + 1:
                return True
        elif inputs.index(k)> len(inputs) - windowSize:
            if d[k] == len(inputs) - inputs.index(k):
                return True
        elif d[k] == windowSize:
            return True
    return False

print(alert([1,8,2,4,5],2,2))

