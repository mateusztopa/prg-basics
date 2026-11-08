def f(amount_to_pay):
    total_coins = 0
    coins_temp = 0
    coins_temp = amount_to_pay / 5
    total_coins += coins_temp
    amount_to_pay - 5 * coins_temp
    coins_temp = amount_to_pay / 2
    total_coins += coins_temp
    amount_to_pay - 2 * coins_temp
    total_coins += amount_to_pay
    return total_coins
ammount = int(input("Enter ammount: "))
result = f(ammount)
print({result})