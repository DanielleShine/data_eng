class Review():
    def __init__(self, content, user, product):
        self.description = content
        self.user = user
        self.product = product

    def __str__(self):
        return f"Review({self.description}, {self.user}, {self.product})"