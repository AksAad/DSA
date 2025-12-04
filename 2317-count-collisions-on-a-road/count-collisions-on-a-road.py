class Solution:
    def countCollisions(self, directions: str) -> int:
        new_dir = directions.lstrip('L')
        new_dir = new_dir.rstrip('R')
        new_dir = new_dir.replace("S","")
        return len(new_dir)