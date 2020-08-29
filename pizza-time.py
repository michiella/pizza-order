from pizzapy import *
from pizzapy import ConsoleInput

def search_menu(menu):
  print("You are now searching the menu.")
  item = input("Type a keyword to search for: ").strip().lower()

  if len(item) > 1:
    item = item[0].upper() + item[1:]
    print(f"Results for: {item}\n")
    menu.search(Name=item)
    print()
  else:
    print("Invalid input.")

def add_to_order(order):
  print("Please type codes of desired items:")
  print("Press ENTER to stop ordering.")
  while True:
    item = input("Code: ").upper()
    try:
      order.add_item(item)
    except:
      if item == "":
        break
      print("Invalid code.")

customer = ConsoleInput.get_new_customer()

my_dominos = StoreLocator.find_closest_store_to_customer(customer)
print(my_dominos)
print("\nClosest store: ")
print(my_dominos)

ans = input("Would you like to order from this store? (y/n)?")
if ans.lower() not in ["yes", "y"]:
  print("Goodbye.")
  quit()

print("\nMENU\n")
menu = my_dominos.get_menu()
order = Order.begin_customer_order(customer,  my_dominos)

while True:
  search_menu(menu)
  add_to_order(order)
  answer = input("Would you like to add more items? (y/n)")
  if answer.lower() not in ["yes", "y"]:
    break

total = 0
print("\nThis is your order: ")
for item in order.data["Products"]:
  price = item["Price"]
  print(item["Name"] + " $" + item["Price"])
  total += float(price)

print("Your total is: $" + str(total) + " TAX.")
payment = input("\nWill you be paying with cash or credit card?")
if payment.lower() in ["card", "credit card"]:
  card = ConsoleInput.get_credit_card()
else:
  card = False

ans = input("Would you like to place this order? (y/n)")
if ans.lower() in ["y", "yes"]:
  order.place(card)
  my_dominos.place_order(order, card)
  print("Order placed!")
else:
  print("Goodbye!")