"""
Test class Vehicle

Attribut:
Vehicle("Renault", "Megan", 3000, 5, 4, "gazole", 1300, 2003, True)

v_marque: NOT NULL    (exemple : "Renault")   ---> String         Marque du véhicule
v_model: NOT NULL     (exemple : "Megan")     ---> String         Modèle du véhicule
v_price: NOT NULL     (exemple : 3000)        ---> Integer        Prix du véhicule
v_place: NOT NULL     (exemple : 5)           ---> Integer        Nombre de places
v_wheels: NOT NULL    (exemple : 4)           ---> Integer        Nombre de roues
v_type: NOT NULL      (exemple : "gazole")    ---> String         Type du moteur
v_weight: NOT NULL    (exemple : 1300)        ---> Integer        Poids du véhicule
v_year: NOT NULL      (exemple : 2003)        ---> Integer        Année du véhicule
v_is_used: NOT NULL   (exemple : True)        ---> Bool           True si c'est d'occasion


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
        self.v = Vehicle("Renault", "Megan", 3000, 5, 4, "gazole", 1300, 2003, True)

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

    def test_price_is_float(self):
        """
        Test if price is float type
        """
        self.assertIs(type(self.v.v_price), float)

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
    #       Tester que la motorisation fait partie du tableau ["diesel", "gazole", "electrique", "hybride"]
    # ____________________________________________________________________
    def test_type_is_valid(self):
        self.assertIn(self.v.v_type, ["diesel", "gazole", "electrique", "hybride"])

    # poids
    #       Tester que le poids est supérieur à 100kg
    # ____________________________________________________________________
    def test_weight_greaterEqual_than_hundred(self):
        """
        test_weight_greater_than_hundred
        """
        self.assertGreaterEqual(self.v.v_weight, 100)

    # year
    #       Tester que l'année est bien un chiffre
    #       Tester que l'année est supérieur à 1769
    # ____________________________________________________________________
    def test_year_is_number(self):
        """
        Test if year is number type
        """
        self.assertIs(type(self.v.v_year), int)

    def test_year_not_before_created_vehicle(self):
        """
        Test year is greater than 1769
        """
        self.assertGreaterEqual(self.v.v_year, 1769)

    # is used
    #       Tester le type est boolean
    # ____________________________________________________________________
    def test_is_used_is_boolean(self):
        """
        Test if is_used is boolean type
        """
        self.assertIs(type(self.v.v_is_used), bool)


if __name__ == '__main__':
    unittest.main()
