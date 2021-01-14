"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
proceeds_str = input('Enter proceeds value: ')
if proceeds_str.isdigit():
    i = 0
    costs_str = input('Enter costs value: ')
    if costs_str.isdigit():
        proceeds_int = int(proceeds_str)
        costs_int = int(costs_str)
        profit_fl = proceeds_int - costs_int
        if profit_fl == 0:
            print('Profit = 0.00, loss = 0.00')
        elif profit_fl < 0:
            print(f'You have bad result:\nLoss={-profit_fl}')
        else:
            count_str = input('Enter count of employees: ')
            if count_str.isdigit():
                count_int = int(count_str)
                profitability_fl = profit_fl / proceeds_int
                profitability_on_employee_fl = profitability_fl / count_int
                print(f'You have positive result:\nProfit: {profit_fl}\nProfitability: {profitability_fl:.2f}')
                print(f'Profitability on one employee: {profitability_on_employee_fl:.4f}')
            else:
                print('Incorrect count value!')
    else:
        print('Incorrect costs value!')
else:
    print('Incorrect proceeds value!')