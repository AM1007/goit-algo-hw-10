# ==== Основи

# import pulp 

# model = pulp.LpProblem("Model Name", pulp.LpMinimize)  # Мінімізація
# # або
# model = pulp.LpProblem("Model Name", pulp.LpMaximize)  # Максимізація

# x = pulp.LpVariable('x', lowBound=0, cat='Continuous')  # x ≥ 0
# y = pulp.LpVariable('y', 3, 7)        # 3 ≤ y ≤ 7

# model += 2 * x + 3 * y, "Problem"  # Мінімізувати або максимізувати 2x + 3y

# model += x + 2 * y <= 8, "Constraint1"
# model += y >= 2, "Constraint2"

# pulp.LpStatus[model.status]

# for variable in model.variables():
#     print(f"{variable.name} = {variable.varValue}")

# # Вартість цільової функції
# print(f"Total cost = {pulp.value(model.objective)}")


# ==== Основи

# import pulp

# # Ініціалізація моделі
# model = pulp.LpProblem("Maximize-Profit", pulp.LpMaximize)

# # Визначення змінних
# A = pulp.LpVariable('A', lowBound=0, cat='Integer')  # Кількість продукту А
# B = pulp.LpVariable('B', lowBound=0, upBound=10, cat='Integer')  # Кількість продукту Б

# # Функція цілі (Максимізація прибутку)
# model += 50 * A + 40 * B, "Profit"

# # Додавання обмежень
# model += 5 * A + 2 * B <= 80  # Обмеження для машини №1
# model += 3 * A + 2 * B <= 40  # Обмеження для машини №2

# # Розв'язання моделі
# model.solve()

# # Вивід результатів
# print("Виробляти продуктів А:", A.varValue)
# print("Виробляти продуктів Б:", B.varValue)


# ==== Рандомізовані алгоритми

# import random

# def is_prime(n, k=5):  # k - кількість ітерацій
#     if n <= 1 or n == 4:
#         return False
#     if n <= 3:
#         return True

#     # Знаходимо r та d
#     d = n - 1
#     r = 0
#     while d % 2 == 0:
#         d //= 2
#         r += 1

#     # Проводимо k тестів
#     for _ in range(k):
#         a = random.randint(2, n - 2)
#         x = pow(a, d, n)
#         if x == 1 or x == n - 1:
#             continue
#         for _ in range(r - 1):
#             x = pow(x, 2, n)
#             if x == n - 1:
#                 break
#         else:
#             return False
#     return True

# # Приклад використання:
# n = 561  # Число Кармайкла
# print(is_prime(n))  # поверне False, хоча 561 - псевдопросте число


# ==== Метод Монте-Карло

# import random

# # Розміри прямокутника
# a = 10  # ширина прямокутника
# b = 5  # висота прямокутника

# def is_inside(a, b, x, y):
#     """Перевіряє, чи знаходиться точка (x, y) всередині трикутника."""
#     return y <= (b / a) * x

# # Генерація випадкових точок
# points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(15000)]

# # Відбір точок, що знаходяться всередині трикутника
# inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]

# # Кількість усіх точок та точок всередині
# N = len(points)
# M = len(inside_points)

# # Теоретична площа трикутника та площа, обчислена методом Монте-Карло
# S = (a * b) / 2  # Теоретична площа
# Sm = (M / N) * (a * b)  # Площа за методом Монте-Карло

# # Виведення результатів
# print(f"Кількість точок всередині трикутника: {M}, загальна кількість точок: {N}")
# print(f"Теоретична площа трикутника: {S}, площа за методом Монте-Карло: {Sm}")
