from bisect import bisect_right

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        full_lakes = {} 
        dry_days = []   

        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
                ans[i] = 1
            else:
                if lake in full_lakes:
                    last_fill = full_lakes[lake]
                    idx = bisect_right(dry_days, last_fill)
                    if idx == len(dry_days):
                        return [] 
                    dry_day_index = dry_days.pop(idx)
                    ans[dry_day_index] = lake  
                full_lakes[lake] = i  
        
        return ans
