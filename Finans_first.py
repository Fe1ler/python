money_capital = 20000
salary = 5000
spend = 6000
increase = 1.05
month = 0

cur_month = money_capital

while cur_month+salary > spend:

    cur_month += salary
    cur_month -= spend
    spend *= increase
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)



















