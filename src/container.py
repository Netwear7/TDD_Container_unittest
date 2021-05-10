"""
Class Container
"""


# Import :
# Class test :
class Container:
    """
    Class Container
    """

    def __init__(self, ctn_type, durability, capacity, capacity_max):
        """
        :param ctn_type: Type of Container
        :param durability: Durability of Container
        :param capacity:  Capacity of Container
        :param capacity_max: max capacity of Container
        """
        self.ctn_type = ctn_type
        self.ctn_durability = durability
        self.ctn_capacity = capacity
        self.ctn_capacity_max = capacity_max

    def drink(self, quantity):
        """
        Drink Container
        :param quantity: quantity drunk of Container.
        """
        self.ctn_capacity -= quantity
        self.ctn_durability -= 1

    def fill(self, quantity):
        """
        Fill Container
        :param quantity: Quantity added to Container.
        """
        self.ctn_capacity += quantity
        self.ctn_durability -= 0.5
        # TODO verifie max added quantity  is not greater than quantity we can add.
