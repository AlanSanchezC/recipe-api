from django.test import TestCase
from app.calc import add, subtract

class CalcTests(TestCase):

    def test_add_numbers(self):
        """ Prueba de suma """
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """ Resta de números """
        self.assertEqual(subtract(11, 5), 6)