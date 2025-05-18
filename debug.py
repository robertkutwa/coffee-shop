# debug.py
from customer import Customer
from coffee import Coffee
from order import Order

customer1 = Customer("Alice")
customer2 = Customer("Bob")


coffee1 = Coffee("Latte")
coffee2 = Coffee("Cappuccino")
coffee3 = Coffee("Espresso")

order1 = Order(customer1, coffee1, 3.5)
order2 = Order(customer1, coffee2, 4.0)
order3 = Order(customer2, coffee1, 3.0)
order4 = Order(customer2, coffee3, 2.5)

print(f"{customer1.name}'s orders: {[o.coffee.name for o in customer1.orders()]}")
print(f"{customer1.name}'s coffees: {[c.name for c in customer1.coffees()]}")
print(f"{coffee1.name}'s customers: {[c.name for c in coffee1.customers()]}")
print(f"{coffee1.name}'s number of orders: {coffee1.num_orders()}")
print(f"{coffee1.name}'s average price: {coffee1.average_price():.2f}")

biggest_latte_fan = Customer.most_aficionado(coffee1)
if biggest_latte_fan:
    print(f"Biggest Latte fan: {biggest_latte_fan.name}")
else:
    print("No one has ordered this coffee yet")