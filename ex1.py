"""
Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом. Оценить эффективность своего решения.

Эффективность O(n) [O(max(len(l1), len(l2)))]
"""


def difference(l1, l2):
    """
        Возращает множество элементов, которые есть в списке l1, но нет в списке l2.

        Args:
            l1: Первый список.
            l2: Второй список.

        Returns:
            Множество элементов, которые есть в списке l1, но нет в l2.
    """
    s1 = set(l1)
    s2 = set(l2)
    return s1 - s2


if __name__ == '__main__':
    assert difference([], []) == set([])
    assert difference([], [1]) == set([])
    assert difference([1], []) == set([1])
    assert difference([1, 2], [1, 2]) == set([])
    assert difference([1, 2], [3, 4]) == set([1, 2])
    assert difference([1, 2, 3, 4, 5], [2, 4]) == set([1, 3, 5])
