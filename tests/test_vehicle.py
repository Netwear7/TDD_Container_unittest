"""
Test class Vehicle

Attribut
marque:
model:
price:
place:
wheels:
type:
weight:
year:
is_used:
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
        self.v = Vehicle("Renault", "Megan", 3000, 5, 4, "diesel", 1300, 2003, True)

    # def tearDown(self):
    #     pass

    # Instance
    #       Tester que c'est la bonne instance utilisée
    # ____________________________________________________________________
    def test_vehicle_is_instance(self):
        """
        Test class is instance of Vehicle.
        """
        self.assertIsInstance(self.v, Vehicle)

    # Marque
    #       Tester Chaine n'est pas vide
    #       (Optionnel) Tester que ça fait bien partie d'une marque dans un tableau
    # ____________________________________________________________________
    def test_marque_is_not_empty(self):
        """
        test_marque_is_not_empty
        """
        temp_marque = self.v.v_marque.strip()
        self.assertNotEqual(temp_marque, "")

    # Model
    #       Tester Chaine n'est pas vide
    #       (Optionnel) Tester qu'un modèle appartient a une marque
    # ____________________________________________________________________
    def test_model_is_not_empty(self):
        """
        test_model_is_not_empty
        """
        temp_model = self.v.v_model.strip()
        self.assertNotEqual(temp_model, "")

    # Prix
    #       Tester que le prix n'est pas égale à 0
    # ____________________________________________________________________
    def test_price_greater_than_zero(self):
        """
        test_price_greater_than_zero
        """
        self.assertGreater(self.v.v_price, 0)

    # nbr_place
    #       Tester que le nbr de place est supérieur à 0.
    # ____________________________________________________________________
    def test_place_greater_than_zero(self):
        """
        test_place_greater_than_zero
        """
        self.assertGreater(self.v.v_place, 0)

    # Wheel
    #       Tester que le nbr de roue est supérieur à 0.
    # ____________________________________________________________________
    def test_wheels_greater_than_zero(self):
        """
        test_wheels_greater_than_zero
        """
        self.assertGreaterEqual(self.v.v_wheels, 2)

    # type_motorisation(diesel)
    # TODO Tester que la motorisation fait partie du tableau ["diesel", "gazole", "electrique", "hybride"]
    # ____________________________________________________________________

    # poids
    #       Tester que le poids est supérieur à 100kg
    # ____________________________________________________________________
    def test_weight_greaterEqual_than_hundred(self):
        """
        test_weight_greater_than_hundred
        """
        self.assertGreaterEqual(self.v.v_weight, 100)

    # year
    # TODO  Tester que l'année est bien un chiffre
    # TODO  Tester que l'année est supérieur à 1900
    # ____________________________________________________________________

    # is used
    # TODO  Tester le type est boolean
    # ____________________________________________________________________


if __name__ == '__main__':
    unittest.main()
