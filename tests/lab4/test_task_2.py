import unittest

from src.lab4.task_2.task_2 import *

class MyTestCase(unittest.TestCase):
    hum1 = Human(5, "men1")
    hum2 = Human(5, "men2")
    hum3 = Human(6, "men3")

    group = Group(1, 150)
    def test_Human_get_print(self):
        self.assertEqual(self.hum1.get_print(), "men1 (5)")

    def test_Human___lt__(self):
        self.assertEqual([self.hum1 < self.hum2, self.hum1 < self.hum3, self.hum2 < self.hum3], [False, True, True])

    def test_Group(self):
        self.group.add(self.hum1)
        self.group.add(self.hum2)
        self.group.add(self.hum3)
        self.assertEqual(self.group.get_print(), "1+: men3 (6), men1 (5), men2 (5)\n")

#     def test_main(self):
#           добавить передачу аргументов командной строки
#         self.assertEqual(main([
# "один один одинович,18",
# "два два двович,36",
# "три три тривеч,54",
# "четыре четыре четырыч,72",
# "пять пять пятыч,90",
# "шесть шесть шестович,108",
# "семь семь семёнов,36",
# "восемь восемь восьмёновичк,35",
# "END"
#         ]),
# """101+: шесть шесть шестович (108)
# 81-100: пять пять пятыч (90)
# 61-80: четыре четыре четырыч (72)
# 46-60: три три тривеч (54)
# 26-35: два два двович (36), семь семь семёнов (36), восемь восемь восьмёновичк (35)
# 0-18: один один одинович (18)""")


if __name__ == '__main__':
    unittest.main()
