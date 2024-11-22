import unittest
from entities.citation import Article
from repositories.citation_repository import generate_bibtex

class TestBibtexGeneration(unittest.TestCase):
    
    def test_generate_bibtex_returns_correctly_formatted_article(self):
        article1 = Article(1, "article1", "John Doe", "Example Article", "Example Journal", 2022, 1, "1-10")
        article2 = Article(2, "article2", "Jane Doe", "Another Example Article", "Another Example Journal", 2023, 2, "11-20")
        citations = [article1, article2]
        expected_bibtex = [
            "@article{article1,\n"
            "    author = {John Doe},\n"
            "    title = {Example Article},\n"
            "    journal = {Example Journal},\n"
            "    year = {2022},\n"
            "    volume = {1},\n"
            "    pages = {1-10}\n"
            "}",
            "@article{article2,\n"
            "    author = {Jane Doe},\n"
            "    title = {Another Example Article},\n"
            "    journal = {Another Example Journal},\n"
            "    year = {2023},\n"
            "    volume = {2},\n"
            "    pages = {11-20}\n"
            "}"
        ]
        bibtex_citations = generate_bibtex(citations)
        self.assertEqual(bibtex_citations, expected_bibtex)

