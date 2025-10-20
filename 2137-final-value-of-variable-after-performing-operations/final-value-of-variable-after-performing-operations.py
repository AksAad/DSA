class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0 
        for i in range(0,len(operations)):
            if operations[i][1] == '+':
                x+=1
            else:
                x-=1
        return x