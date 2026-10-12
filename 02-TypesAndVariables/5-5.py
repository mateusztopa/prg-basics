price = float(input("Enter price: "))
discount = int(input("Enter discount: "))
Reduction = price * (discount) / 100
Price_with_discount = price - Reduction
print(f"Price with discount: {round(Price_with_discount,2)}")
print(f"Reduction {round(Reduction,2)}")