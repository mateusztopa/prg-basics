number_of_products = int(input("Number of products putrchased: "))
product_price = float(input("Product price: "))
ammount_to_pay = 0
for i in range(1 , number_of_products + 1):
    if i > 2:
        ammount_to_pay += product_price * 0.75
    else:
        ammount_to_pay += product_price
print(f"Amount to pay: {round(ammount_to_pay)}")