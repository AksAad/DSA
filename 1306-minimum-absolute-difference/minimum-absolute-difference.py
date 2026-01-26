class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        minDiff = float('inf')
        res = []
        for i in range(1, n):
            diff = arr[i] - arr[i - 1]
            if diff < minDiff:
                minDiff = diff
                res = [[arr[i - 1], arr[i]]]
            elif diff == minDiff:
                res.append([arr[i - 1], arr[i]])
        return res
