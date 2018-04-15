# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        d = {}
        res = []
        m = -1
        for i in range(len(intervals)):
            if intervals[i].start > m:
                m = intervals[i].start
            if intervals[i].start not in d:
                d[intervals[i].start] = i
        for i in intervals:
            print(i.end in d)
            if i.end in d:
                res.append(d[i.end])
            else:
                if i.end > m:
                    res.append(-1)
                else:
                    temp = i.end + 1
                    b = False
                    while temp <= m:
                        if temp in d:
                            b = True
                            res.append(d[temp])
                            break
                        temp+=1
                    if not b:
                        res.append(-1)
        return res
