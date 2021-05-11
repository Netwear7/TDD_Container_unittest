"""
Class Vehicle
"""


# Import :
# Class test :
class Vehicle:
    """
    Class Vehicle.
    """

    def __init__(self, marque, model, price, place, wheels, type, weight, year, is_used):
        """
        :param marque: Marque du véhicule
        :param model: Modèle du véhicule
        :param price: Prix du véhicule
        :param place: Nombre de places
        :param wheels: Nombre de roues
        :param type: Type du moteur
        :param weight: Poids du véhicule
        :param year: Année du véhicule
        :param is_used: True si c'est d'occasion
        """
        self.v_marque = marque
        self.v_model = model
        self.v_price = price
        self.v_place = place
        self.v_wheels = wheels
        self.v_type = type
        self.v_weight = weight
        self.v_year = year
        self.v_is_used = is_used
