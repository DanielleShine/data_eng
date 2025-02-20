class Product():
    def __init__(self, name, description, seller, price, available=True):
        self.name = name
        self.model_number = description
        self.seller = seller
        self.price = price
        self.available = available
        self.reviews = []

    def __str__(self):
        return f"Product({self.name}, {self.description}) at {self.price}"