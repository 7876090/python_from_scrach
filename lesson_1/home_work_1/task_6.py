"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который
общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и
выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:

1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
progress_int = 10
a_str = input('Enter first day result: ')
if a_str.isdigit():
    b_str = input('Enter minimal result: ')
    if b_str.isdigit():
        a_fl = float(a_str)
        b_fl = float(b_str)
        if b_fl == a_fl:
            print('minimal result = first day result')
        elif b_fl < a_fl:
            print('first day result > minimal result')
        else:
            print(f'1 day: {a_fl:.2f}')
            i = 1;
            while a_fl < b_fl:
                i += 1
                a_fl = a_fl + a_fl * progress_int / 100;
                print(f'{i} day: {a_fl:.2f}')
    else:
        print('Incorrect minimal result!')
else:
    print('Incorrect day result value!')