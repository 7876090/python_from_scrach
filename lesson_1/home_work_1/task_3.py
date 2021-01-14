"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""

n_str = input('Enter number: ')
if n_str.isdigit():
    result_int = int(n_str) + int(n_str * 2) + int(n_str * 3)
    print(result_int)
else:
    print('Incorrect value!')