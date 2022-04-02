import unittest


class TestAbs(unittest.TestCase):  # создаем отдельный класс для набора тестов
    def test_ads1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()
