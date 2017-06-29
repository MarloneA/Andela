class ShoppingCart(object):

    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        self.total += (price * quantity)
        self.items[item_name] = quantity

    def remove_item(self, item_name, quantity, price):
        current_item_quantity = self.items[item_name]
        if quantity >= current_item_quantity:
            self.total -= (price * current_item_quantity)
            del self.items[item_name]
        else:
            updated_item_quantity = (current_item_quantity - quantity)
            self.total -= (price * quantity)
            self.items[item_name] = updated_item_quantity

    def checkout(self, cash_paid):
        if cash_paid < self.total:
            return "Cash paid not enough"
        else:
            balance = (cash_paid - self.total)
            return balance

class Shop(ShoppingCart):

    def __init__(self):
        self.quantity = 100

    def remove_item(self):
        self.quantity -= 1
