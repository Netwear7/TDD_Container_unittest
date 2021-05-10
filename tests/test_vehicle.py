"""
Test class Vehicle
"""

# Import :
import unittest
# Modification d'un lien relatif
import sys
sys.path.append("..")

# Import Class to test:
from src.vehicle import Vehicle


# Class test :
class TestVehicle(unittest.TestCase):
    """
    TDD on class Container
    """

    def setUp(self):
        """
        Method called to prepare the test fixture.
        """
        # Marque, Modele, Prix, nbr_place, roue, type_motorisation(diesel), poids, year, is used
        self.v = Vehicle("Renault", "Megan", 3000, 5, 4, "Diesel", 1300, 2003, True)

    # def tearDown(self):
    #     pass

    def test_vehicle_is_instance(self):
        """
        Test class is instance of Vehicle.
        """
        self.assertIsInstance(self.v, Vehicle)

    def test_marque_is_not_empty(self):
        temp_marque = self.v.v_marque.strip()
        self.assertNotEqual(temp_marque, "")
        # self.assertNotEqual(self.v.v_marque, "")





    def test_price_greater_than_zero(self):
        """
        test_price_greater_than_zero
        """
        self.assertGreater(self.v.v_price, 0)


if __name__ == '__main__':
    unittest.main()

# test:
    # Instance
        # Tester que c'est la bonne instance utilisée

    # Marque
        # Tester Chaine n'est pas vide
        # Tester que ça fait bien partie d'une marque dans un tableau
    # Modele
        # Tester Chaine n'est pas vide
        # Tester qu'un modèle appartient a une marque
    # Prix
        # Tester que le prix n'est pas égale à 0
    # nbr_place
        # Tester que le nbr de place est supérieur à 0.
    # roue
        # Tester que le nbr de roue est supérieur à 0.
    # type_motorisation(diesel)
        # Tester que la motorisation fait partie du tableau ["diesel", "gazole", "electrique", "hybride"]
    # poids
        # Tester que le poids est supérieur à 100kg
    # year
        # Tester que l'année est bien un chiffre
        # Tester que l'année est supérieur à 1900
    # is used
        # Tester le type est boolean