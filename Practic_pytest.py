import pytest
from Practic import *


def test_spisok():
    assert spisok([1, 2, 3], [2, 3, 4]) == [2, 3]


def test_stroka():
    assert stroka(['Привет', 'Пока', 'Егор', 'Овен', 'Автобус']) == ['Егор', 'Овен', 'Автобус']


@pytest.mark.parametrize('n, expected', [(1, 1), (10, 55)])
def test_fibo(n, expected):
    assert fibo(n) == expected