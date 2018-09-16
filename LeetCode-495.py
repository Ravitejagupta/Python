class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0
        r = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1] - timeSeries[i] >= duration:
                r += duration
            else:
                r += timeSeries[i+1] - timeSeries[i]
        return r + duration
