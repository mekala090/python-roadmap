class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def is_long(self):
        return self.pages > 300

    def discounted_price(self, percent):
        return self.price - self.price * percent / 100

    def display(self):
        print(f"'{self.title}' by {self.author} | {self.pages} pages | Rs.{self.price} | "
              f"Long: {self.is_long()} | After 10% off: Rs.{self.discounted_price(10):.2f}")


