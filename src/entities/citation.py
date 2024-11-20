class Article:
    def __init__(self, *a):
        self.id = a[0]
        self.key = a[1]
        self.author = a[2]
        self.title = a[3]
        self.journal = a[4]
        self.year = a[5]
        self.volume = a[6]
        self.pages = a[7]

    def __str__(self):
        return f'{self.author}: {self.title} ({self.key})'
