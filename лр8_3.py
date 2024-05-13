def calculate_investment_amount(initial_amount, interest_rate, years):
    # Формула для сложного процента: A = P(1 + r)^n
    # где A - итоговая сумма, P - начальная сумма, r - процентная ставка в виде десятичной дроби, n - количество лет
    amount = initial_amount * (1 + interest_rate) ** years
    return amount

initial_amount = float(input("Введите начальную сумму: "))
interest_rate = float(input("Введите процентную ставку (в виде десятичной дроби): "))
years = int(input("Введите количество лет: "))

final_amount = calculate_investment_amount(initial_amount, interest_rate, years)
print("Через", years, "лет ваша инвестиция вырастет до:", "{:.2f}".format(final_amount))
