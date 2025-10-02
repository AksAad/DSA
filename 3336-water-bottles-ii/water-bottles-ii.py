class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total_drink = numBottles
        #numBottles to be the total empty bottles
        while numBottles >= numExchange:
            total_drink += 1
            numBottles += 1
            numBottles = numBottles - numExchange
            numExchange += 1
        return total_drink