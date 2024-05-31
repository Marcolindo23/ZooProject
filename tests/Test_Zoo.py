import unittest
from unittest import TestCase
from src.Zoo import Zoo, ZooKeeper, Animal, Fence
class TestZoo(TestCase):


    def setUp(self):
        
        self.zoo_1: Zoo = Zoo()
        self.ZooKeeper_1: ZooKeeper = ZooKeeper(name = "Gianni", surname = "Rossi", id = 1)
        self.Fence_1: Fence = Fence(area = 100, temeprature = 25.0, habitat = "Savana")
        self.animal_1: Animal = Animal(name = "Pluto", species = "Canide", age = 5, height = 300.0, width = 1.8, preferred_habitat = "Savaan")

    def test_1(self):

        self.ZooKeeper_1.add_animal(self.animal_1, self.Fence_1)
        result: int = len(self.Fence_1.animals)
        message: str = f"Error: The function add animal should not add self.animal_1 into self.fence_1"

        self.assertEqual(result, 0, message)

    def test_2(self):
        self.ZooKeeper_1.add_animal(self.animal_1, self.Fence_1)
        self.ZooKeeper_1.add_animal(self.animal_1, self.Fence_1)
        result: int = len(self.Fence_1.animals)
        message: str = f"Error: The function add animal should not add self.animal_1 into self.fence_1 twice"

        self.assertEqual(result, 1, message)

    def test_3(self):
        self.ZooKeeper_1.add_animal(self.animal_2, self.Fence_2)
        result: int = len(self.Fence_2.animals)
        message: str = f"Error: The function add animal should add self.animal_2 into self.fence_2"

        self.assertEqual(result, 1, message)


    def test_4(self):
        self.ZooKeeper_1.add_animal(self.animal_1, self.Fence_1)
        self.ZooKeeper_1.remove_animal(self.animal_1, self.Fence_1)
        result: int = len(self.Fence_1.animals)
        message: str = f"Error: The function remove animal should remove self.animal_1 from self.fence_1"

        self.assertEqual(result, 0, message)

    def test_5(self):
        self.ZooKeeper_1.add_animal(self.animal_1, self.Fence_1)
        self.ZooKeeper_1.remove_animal(self.animal_2, self.Fence_1)
        result: int = len(self.Fence_1.animals)
        message: str = f"Error: The function remove animal should not remove self.animal_2 from self.fence_1 as it was not present"

        self.assertEqual(result, 1, message)


    def test_6(self):
        self.Fence_3.max_animals = 2
        self.ZooKeeper_1.add_animal(self.animal_1, self.Fence_3)
        self.ZooKeeper_1.add_animal(self.animal_2, self.Fence_3)
        self.ZooKeeper_1.add_animal(self.animal_3, self.Fence_3)
        result: int = len(self.Fence_3.animals)
        message: str = f"Error: The function add animal should not add self.animal_3 into self.fence_3 as it exceeds the max limit"

        self.assertEqual(result, 2, message)









if __name__== "__main__":
    unittest.main()