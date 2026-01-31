class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        curr = letters[0]
        flag = False
        for c in letters:
            if not flag:
                if c > target:
                    curr = c
                    flag = not flag
            else:
                if c > target and c < curr:
                    curr = c
        return curr
            