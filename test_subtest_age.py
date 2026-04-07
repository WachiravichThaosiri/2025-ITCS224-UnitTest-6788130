import unittest
from age import categorize_by_age


class TestIschild(unittest.TestCase):
    def test_child_age(self):
        print()
        for age in range(0, 9):
            with self.subTest(age=age):
                print(age, "is consider as a child")

if __name__ == "__main__":
    unittest.main(verbosity=2)
