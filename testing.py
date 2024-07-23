subtotal = float(input('Enter subtotal: '))
tax_percentage = float(input('Enter sales tax percentage: '))
total = subtotal + (subtotal * (tax_percentage*.01))
print("Your total bill is: $", total)
answer = input("Would you like to tip before or after tax? (please enter before or after) ")

if answer == 'after':
    percent_tip = float(input("How many percent do you want to tip? "))
    final_total = total + (total * (percent_tip*.01))
    print("Your final total is: $", final_total)

if answer == 'before':
    percent_tip = float(input("How many percent do you want to tip? "))
    final_total = total + (subtotal * (percent_tip*.01))
    print("Your final total is: $", final_total)