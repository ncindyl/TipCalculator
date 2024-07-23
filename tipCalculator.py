bill = float(input("Enter bill amount: "))
tax = float(0.0625)
graitude_percent = float(input("How many percent for tips: "))
graitude_percent = graitude_percent / 100

tip = float((bill - tax * bill) * graitude_percent)

print("Tip: ", tip)
print("subtotal: ", bill + tip)
