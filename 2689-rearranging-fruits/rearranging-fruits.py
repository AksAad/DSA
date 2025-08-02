class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        counts1 = Counter(basket1)
        counts2 = Counter(basket2)
        excess1 = []
        excess2 = []
        j = 0
        for fruit in set(counts1) | set(counts2):
            if (counts1[fruit] + counts2[fruit]) %2 != 0:
                return -1
                break
            total = counts1[fruit] + counts2[fruit]
            target = total//2
            if (counts1[fruit] > target):
                diff = counts1[fruit] - target
                excess1.extend([fruit] * diff)
            if (counts2[fruit] > target):
                diff = counts2[fruit] - target
                excess2.extend([fruit] * diff)
        excess1.sort()
        excess2.sort(reverse=True)
        global_min = min(basket1 + basket2)
        proxy_swap_cost = 2 * global_min
        total_cost = 0
        for fruit1,fruit2 in zip(excess1, excess2):
            direct_swap_cost = min(fruit1,fruit2)
            if proxy_swap_cost > direct_swap_cost:
                cheaper = direct_swap_cost
            else:
                cheaper = proxy_swap_cost
            total_cost += cheaper
        return total_cost