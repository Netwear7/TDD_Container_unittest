"""
Test class Container
"""

# Import :
import unittest
# Modification d'un lien relatif
import sys
sys.path.append("..")

# Import Class to test:
from src.container import Container


# Class test :
class TestContainer(unittest.TestCase):
    """
    TDD on class Container
    """
    def setUp(self):
        """
        Method called to prepare the test fixture.
        """
        # ctn_type / durability / capacity ml / capacity_max
        self.c = Container("Bouteille", 30, 50, 100)

    def tearDown(self):
        self.c.ctn_durability = 30
        self.c.ctn_capacity = 50
        self.c.ctn_capacity_max = 100

    def test_container_is_instance(self):
        """
        Test class is instance of Container.
        """
        self.assertIsInstance(self.c, Container)

    def test_durability_after_drink(self):
        """
        Test durability after drink.
        if player drink, durability -1
        """
        # Durabilité avant drink()
        temp_durability = self.c.ctn_durability
        self.c.drink(25)
        # La durabilité doit baisser
        self.assertEqual(self.c.ctn_durability, temp_durability - 1)

    def test_durability_after_fill_in(self):
        """
        Test durability after fill container.
        if player fill container, durability - 0.5
        """
        # Durabilité avant drink()
        temp_durability = self.c.ctn_durability
        # Capacité restante pour remplir la bouteille:
        temp_fill = self.c.ctn_capacity_max - self.c.ctn_capacity
        self.c.fill(temp_fill)
        # La durabilité doit baisser
        self.assertEqual(self.c.ctn_durability, temp_durability - 0.5)

    def test_is_broken(self):
        """
        Test if Container is broken
        """
        self.c.ctn_durability = 1
        self.c.drink(25)
        self.assertLessEqual(self.c.ctn_durability, 0)


if __name__ == '__main__':
    unittest.main()
