def minCostClimbingStairs(cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        result = [10000]*(len(cost))
        result[0] = cost[0]
        result[1] = cost[1]
        for i in range(2,len(cost)):
            result[i] = min(result[i-1]+ cost[i],result[i-2]+ cost[i])
        print(result)
        return(min(result[len(cost)-1],result[len(cost)-2]))
