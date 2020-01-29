class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices%2 == 1:
            return []
        if tomatoSlices < 2*cheeseSlices or tomatoSlices > 4*cheeseSlices:
            return []
        return [(tomatoSlices-2*cheeseSlices)//2 , cheeseSlices - (tomatoSlices-2*cheeseSlices)//2]
