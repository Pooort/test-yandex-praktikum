"""
Дан массив целых чисел. Нужно удалить из него нули. Можно использовать только О(1) дополнительной памяти.
"""


def delete_zero(l):
    """
        Возращает список без нулей.

        Args:
            l: Список целых чисел.

        Returns:
            Исходный список без нулей.
    """
    while True:
        try:
            l.remove(0)
        except ValueError:
            break
    return l


if __name__ == '__main__':
    assert delete_zero([0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]) == [1, 4, 5, 6, 7, 8, -4]
