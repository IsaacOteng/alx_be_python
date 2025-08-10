class Book:
    def __init__(self, titlw, author, year):
        self.title = titlw
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"{sel.title} by {self.author}, published in {self.year}"
    
    def __del__(self):
        return f"Deleting {self.title}"
    
    