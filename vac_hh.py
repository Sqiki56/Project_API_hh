from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        # Преобразуем числа в строки
        nums_str = list(map(str, nums))
        
        # Определяем функцию сравнения
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Сортируем строки с использованием пользовательского компаратора
        nums_str.sort(key=cmp_to_key(compare))
        
        # Объединяем отсортированные строки
        result = ''.join(nums_str)
        
        # Убираем ведущие нули (если результат начинается с нуля, то возвращаем "0")
        return result if result[0] != '0' else "0"
