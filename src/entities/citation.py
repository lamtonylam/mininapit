from util import string_or_empty_string

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

    def bibtex(self):
        return (
            f'@{self.type_as_string}{{{self.key},\n'
            f'  author = {{{self.author}}},\n'
            f'  title = {{{self.title}}},\n'
            f'  journal = {{{self.journal}}},\n'
            f'  year = {{{self.year}}},\n'
            f'  volume = {{{string_or_empty_string(self.volume)}}},\n'
            f'  pages = {{{string_or_empty_string(self.pages)}}}\n'
            f'}}'
        )

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

    def bibtex(self):
        return (
            f'@{self.type_as_string}{{{self.key},\n'
            f'  author = {{{self.author}}},\n'
            f'  title = {{{self.title}}},\n'
            f'  year = {{{self.year}}},\n'
            f'  booktitle = {{{self.booktitle}}}\n'
            f'}}'
        )
