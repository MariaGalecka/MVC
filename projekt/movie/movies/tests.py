from django.test import TestCase
from .models import Movie

class MovieModelTest(TestCase):
    def test_string_representation(self):
        movie = Movie(title="Matrix", director="Wachowski", rating=9.0)
        self.assertEqual(str(movie), "Matrix (Wachowski)")
