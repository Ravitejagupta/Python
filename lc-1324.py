def printVertically(s):
    r = []
    cur = 0
    for index, word in enumerate(s.split()):
        for i in range(len(word)):
            if i < cur:
                r[i] += word[i]
            else:
                r.append(" "*index+ word[i])
                cur += 1
        l = len(word)
        while cur-l >0:
            r[l] += " "
            l += 1
    return [c.rstrip() for c in r]

print(printVertically("TO BE OR NOT TO BE"))
