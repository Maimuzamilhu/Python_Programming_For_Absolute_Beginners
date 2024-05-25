"""Advanced Question: Online Shopping Cart
You are building an online shopping cart system. Consider the following features:
Each product has a name, price, and category.
Implement a decorator called Discount that applies percentage-based discounts to products.
Use abstraction to create an interface for payment methods (e.g., credit card, PayPal).
Handle file I/O for storing product details and user orders.
Implement error handling for cases like invalid payment details or out-of-stock products.
How would you ensure encapsulation while handling user orders and payments?
"""

from abc import ABC, abstractmethod

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class Discount:
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    def apply_discount(self, product):
        product.price -= product.price * self.discount_rate

class PaymentInterface(ABC):
    @abstractmethod
    def process_payment(self):
        pass

class CreditCardPayment(PaymentInterface):
    def process_payment(self):
        print("Processing credit card payment...")

class PayPalPayment(PaymentInterface):
    def process_payment(self):
        print("Processing PayPal payment...")

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def checkout(self, payment_method):
        payment_method.process_payment()
        for product in self.products:
            print(f"Purchased: {product.name} - ${product.price}")

class FileIO:
    @staticmethod
    def store_product_details(product):
        with open('product_details.txt', 'a') as file:
            file.write(f"{product.name}, {product.price}, {product.category}\n")

    @staticmethod
    def store_user_order(product):
        with open('user_orders.txt', 'a') as file:
            file.write(f"{product.name}, {product.price}\n")

class OutOfStockError(Exception):
    pass

class ShoppingCartError(Exception):
    pass

class ShoppingCartManager:
    def __init__(self):
        self.stock = {'product1': 10, 'product2': 5}

    def process_order(self, product):
        if product.name in self.stock and self.stock[product.name] > 0:
            self.stock[product.name] -= 1
            FileIO.store_user_order(product)
        else:
            raise OutOfStockError("Product is out of stock")

product1 = Product("Laptop", 1000, "Electronics")
product2 = Product("Shoes", 50, "Fashion")

discount = Discount(0.1)
discount.apply_discount(product1)

credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

cart = ShoppingCart()
cart.add_product(product1)
cart.add_product(product2)

cart.checkout(credit_card_payment)

manager = ShoppingCartManager()
manager.process_order(product1)
