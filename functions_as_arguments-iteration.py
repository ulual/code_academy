def total_bill(func, value):
    total = func(value)
    return total
    
def add_tax(total):
  tax = total * 0.06
  new_total = total + tax
  return new_total

def add_tip(total):
  tip = total * .2
  new_total = total + tip
  return new_total
  
def total_bills(func, list):
  # This list will store all the new bill values
  new_bills = []

  # This loop will iterate through our bills
  for i in range(len(list)):

    # Here we apply the function to each element of the list!
    total = func(list[i])
    new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

  return new_bills

bills = [115, 120, 42]
 
bills_w_tip = total_bills(add_tip, bills)
 
print(bills_w_tip)