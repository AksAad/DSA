class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total_drink = numBottles
        #hereforth numBottles is the same as the total number of empty bottles
        while numBottles >= numExchange:
            total_drink += 1
            numBottles += 1
            numBottles -= numExchange
            numExchange += 1
        return total_drink