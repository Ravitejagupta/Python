class Solution:
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        d={}
        def flag(a,b,di):
            c = 0
            for i in range(a,b):
                if i in di:
                    c = max(c,di[i])
            if c == 0:
                return [1,-1]
            else:
                return [0,c]
        r = []
        for box in positions:
            if box[0] not in d and (box[0]+box[1]-1) not in d:
                if flag(box[0],box[0]+box[1], d)[0] == 1:
                    for i in range(box[0],box[0]+box[1]):
                        d[i] = box[1]
                    if r == []:
                        r.append(box[1])
                    else:
                        r.append(max(r[-1],box[1]))
                    print("case 1")
                else:
                    extra = flag(box[0],box[0]+box[1], d)[1]
                    for i in range(box[0],box[0]+box[1]):
                        d[i] = box[1] + extra
                    if r == []:
                        r.append(box[1]+extra)
                    else:
                        r.append(max(r[-1],box[1]+extra))
                    print("case 5")
            elif box[0] in d and (box[0]+box[1]-1) in d:
                farzi = flag(box[0],box[0]+box[1], d)
                if farzi[0] == 0:
                    step = farzi[1] + box[1]
                    for i in range(box[0],box[0]+box[1]):
                        d[i] = step
                else:
                    step = max(d[box[0]],d[box[0]+box[1]-1]) + box[1]
                    for i in range(box[0],box[0]+box[1]):
                        d[i] = step
                if r == []:
                    r.append(step)
                else:
                    r.append(max(r[-1],step))
                print("case 2")
                
                
            elif box[0] in d and (box[0]+box[1]-1) not in d:
                farzi = flag(box[0],box[0]+box[1], d)
                if farzi[0] == 0:
                    step = farzi[1] + box[1]
                    for i in range(box[0],box[0]+box[1]):
                        d[i] = step
                else:
                    step = d[box[0]] + box[1]
                    for i in range(box[0],box[0]+box[1]):
                        d[i] = step
                if r == []:
                    r.append(step)
                else:
                    r.append(max(r[-1],step))
                print("case 3")
            elif box[0] not in d and (box[0]+box[1]-1) in d:
                farzi = flag(box[0],box[0]+box[1], d)
                if farzi[0] == 0:
                    step = farzi[1] + box[1]
                    for i in range(box[0],box[0]+box[1]):
                        d[i] = step
                else:
                    step = d[box[0]+box[1]-1] + box[1]
                    for i in range(box[0],box[0]+box[1]):
                        d[i] = step             
                if r == []:
                    r.append(step)
                else:
                    r.append(max(r[-1],step))
                print("case 4")
        return r
