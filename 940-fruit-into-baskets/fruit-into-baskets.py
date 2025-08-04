class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = {}
        right = 0
        left = 0
        max_fruits = 0
        for right in range(len(fruits)):
            fruit = fruits[right]
            fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
            if len(fruit_count) > 2:
                while len(fruit_count) > 2:
                    left_fruit = fruits[left]
                    fruit_count[left_fruit] -= 1
                    if fruit_count[left_fruit] == 0:
                        del fruit_count[left_fruit]
                    left += 1
            current_window_size = right - left + 1
            max_fruits = max(max_fruits, current_window_size)
        return max_fruits
                    
