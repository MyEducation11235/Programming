import unittest
from src.lab4.task_1.task_1 import HistoryDatabase


class MyTestCase(unittest.TestCase):
    base = HistoryDatabase()

    def test_read_films(self):
        self.assertEqual(self.base.films, {
            1: "Мстители: , Финал",
            2: "Хатико",
            3: "Дюна",
            4: "Унесенные призраками"
        })

    def test_read_history(self):
        self.assertEqual(self.base.history, [
            frozenset({1, 2, 3}),
            frozenset({1, 3, 4}),
            frozenset({2, 3})
        ])

    def test_get_advice(self):
        self.assertEqual(self.base.get_advice(frozenset([2, 4])), "Дюна")


if __name__ == '__main__':
    unittest.main()
