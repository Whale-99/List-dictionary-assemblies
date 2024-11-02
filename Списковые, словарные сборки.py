# Заданные списки
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Список длин строк в first_strings с длиной >= 5
first_result = [len(word) for word in first_strings if len(word) >= 5]

# 2. Список пар слов одинаковой длины из first_strings и second_strings
second_result = [(word1, word2) for word1 in first_strings for word2 in second_strings if len(word1) == len(word2)]

# 3. Словарь, где ключ - строка, значение - длина строки для строк с чётной длиной
third_result = {word: len(word) for word in first_strings + second_strings if len(word) % 2 == 0}

# Вывод результатов
print(first_result)      # [10, 8, 8]
print(second_result)     # [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
print(third_result)      # {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}
