import unittest
from Practic import *


class Spisok_test(unittest.TestCase):

    def test_spisok(self):
        self.assertEqual(spisok([1, 2, 3], [2, 3, 4]), [2, 3])


class Stroka_test(unittest.TestCase):

    def test_stroka(self):
        self.assertEqual(stroka(['Привет', 'Пока', 'Егор', 'Овен', 'Автобус']), ['Егор', 'Овен', 'Автобус'])


class Fibo_test(unittest.TestCase):

    def test_fibo(self):
        self.assertEqual(fibo(10), 55)