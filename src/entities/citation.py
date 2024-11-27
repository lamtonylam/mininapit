# pylint: disable=too-many-instance-attributes, too-few-public-methods
# let's fix these later

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
        self.type_as_string = 'article'

    def __str__(self):
        return f'{self.author}: {self.title} ({self.key})'

class Inproceedings:
    def __init__(self, *a):
        self.id = a[0]
        self.key = a[1]
        self.author = a[2]
        self.title = a[3]
        self.year = a[4]
        self.booktitle = a[5]
        self.type_as_string = 'inproceedings'

    def __str__(self):
        return f'{self.author}: {self.title} ({self.key})'
