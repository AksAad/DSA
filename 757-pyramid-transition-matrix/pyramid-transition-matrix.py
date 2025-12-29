class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        #post order left right top
        table = defaultdict(set)
        for u,v,w in allowed:
            table[u,v].add(w)
        visited = set()
        def add_neighbour(node):
            res = ['']
            for i in range(1,len(node)):
                curr = table[(node[i-1], node[i])]
                if curr:
                    res = [a+e for e in curr for a in res]
                else:
                    return []
            return res
        def dfs(node):
            if len(node) == 1:
                return True
            if node in visited:
                return False
            for nxt in add_neighbour(node):
                if dfs(nxt):
                    return True
            visited.add(node)
            return False
        return dfs(bottom)