from pizzapy import *

customer = Customer('Michelle', 'Feng', 'michelle.feng@live.ca', '6137629672', '80 St Patrick St, Toronto, ON, M5T2X6')
my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
menu = my_local_dominos.get_menu()
menu.search(Name='Coke')

