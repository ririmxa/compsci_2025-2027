class Order:
    next_order_num = 1
    def __init__(self):
        self.id = Order.next_order_num
        self.order_items = []
        Order.next_order_num += 1
    def add_item(self, item, price):
        self.order_items.append(OrderItems(item, price))
    def __str__(self):
        print(f"My order is:{[*self.order_items]}")
class OrderItems:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price
    def __str__(self):
        print(f"{self.product_name} costs {self.price}")

bobby_pin = Order()
bobby_pin.add_item("computer", 150)
bobby_pin.add_item("whiteboard", 80)
bobby_pin.add_item("bobby pin", 1)
print(bobby_pin)