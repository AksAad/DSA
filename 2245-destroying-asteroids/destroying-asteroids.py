class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        destroyed = True
        asteroids.sort()
        for i in range(0,len(asteroids)):
            if mass >= asteroids[i]:
                mass += asteroids[i]
            else:
                destroyed = False
                return destroyed
        return destroyed