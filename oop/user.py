from review import Review
from product import Product

class User():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.reviews = []

    def write_review(self, content, product):
        review = Review(content, self, product)
        self.reviews.append(review)
        product.reviews.append(review)
        return review

    def buy_product(self, product):
        if product.available:
            print(f"{self.name} bought {product.name}")
            product.available = False
        else:
            print(f"{product.name} is out of stock")

    def sell_product(self,name, description, price):
        product = Product(name, description, price, self, available=True)
        print(f"{self.name} is selling {product.name}")
        return product

    def __str__(self):
        return f"User({self.id}, {self.name})"