import unittest
from age import categorize_by_age


class TestIschild(unittest.TestCase):
    def test_child_age(self):
        print()
        for age in range(0, 9):
            with self.subTest(age=age):
                print(age, "is consider as a child")

class TestIsadult(unittest.TestCase):
    def test_adult_age(self):
        print()
        for age in range(60, 70):
            with self.subTest(age=age):
                print(age, "is consider as a adult")

class TestIsgolden(unittest.TestCase):
    def test_golden_age(self):
        print()
        for age in range(90, 120):
            with self.subTest(age=age):
                print(age, "is consider as a golden")


if __name__ == "__main__":
    unittest.main(verbosity=2)
