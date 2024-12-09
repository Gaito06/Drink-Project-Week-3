import unittest
from Drinks import Drink, Food, Order

class TestDrink(unittest.TestCase):
    def test_get_base(self):
        """Test the getter for base."""
        drink = Drink("hill fog", size="medium")
        self.assertEqual(drink.get_base(), "hill fog")
    
    def test_get_flavors_empty(self):
        """Test the getter for flavors when no flavors are added."""
        drink = Drink("hill fog", size="medium")
        self.assertEqual(drink.get_flavors(), [])
    
    def test_get_size(self):
        """Test the getter for size."""
        drink = Drink("hill fog", size="medium")
        self.assertEqual(drink.get_size(), "medium")
    
    def test_get_total(self):
        """Test the total cost calculation, including flavors."""
        drink = Drink("hill fog", size="medium")
        drink.add_flavor("lemon")
        self.assertEqual(drink.get_total(), 1.75 + 0.15)
    
    def test_set_size(self):
        """Test setting the size."""
        drink = Drink("hill fog", size="medium")
        drink.set_size("large")
        self.assertEqual(drink.get_size(), "large")
    
    def test_invalid_base(self):
        """Test invalid base."""
        with self.assertRaises(ValueError):
            drink = Drink("invalid base", size="medium")
    
    def test_invalid_size(self):
        """Test invalid size."""
        with self.assertRaises(ValueError):
            drink = Drink("hill fog", size="extra large")


class TestFood(unittest.TestCase):
    def test_get_food_type(self):
        """Test the getter for food type."""
        food = Food("hotdog")
        self.assertEqual(food.get_food_type(), "hotdog")
    
    def test_add_topping(self):
        """Test adding valid toppings to food."""
        food = Food("french fries")
        food.add_topping("nacho cheese")
        self.assertIn("nacho cheese", food.get_toppings())
    
    def test_add_invalid_topping(self):
        """Test adding an invalid topping to food."""
        food = Food("french fries")
        with self.assertRaises(ValueError):
            food.add_topping("invalid topping")
    
    def test_get_total(self):
        """Test the total cost of food including toppings."""
        food = Food("french fries")
        food.add_topping("nacho cheese")
        food.add_topping("chili")
        self.assertEqual(food.get_total(), 1.50 + 0.30 + 0.60)
    
    def test_get_price(self):
        """Test the price of the base food item."""
        food = Food("corndog")
        self.assertEqual(food.get_price(), 2.00)
    
    def test_topping_count(self):
        """Test the number of toppings added to food."""
        food = Food("ice cream")
        food.add_topping("whipped cream")
        food.add_topping("chocolate sauce")
        self.assertEqual(food.get_topping_count(), 2)


class TestOrder(unittest.TestCase):
    def test_get_items(self):
        """Test the getter for items in the order."""
        order = Order()
        drink1 = Drink("hill fog", size="medium")
        food1 = Food("hotdog")
        order.add_item(drink1)
        order.add_item(food1)
        self.assertEqual(order.get_items(), [drink1, food1])
    
    def test_get_total(self):
        """Test the total calculation for the order."""
        order = Order()
        drink1 = Drink("hill fog", size="medium")
        drink2 = Drink("Mr. Salt", size="large")
        food1 = Food("french fries")
        food1.add_topping("chili")
        food2 = Food("ice cream")
        order.add_item(drink1)
        order.add_item(drink2)
        order.add_item(food1)
        order.add_item(food2)
        
        expected_total = (1.75 + 0.15) + (2.05 + 0.15) + (1.50 + 0.60) + 3.00  # Drink + food prices
        expected_total_with_tax = expected_total * (1 + 0.0725)
        self.assertAlmostEqual(order.get_total(), expected_total_with_tax, places=2)
    
    def test_get_receipt(self):
        """Test the receipt generation."""
        order = Order()
        drink1 = Drink("hill fog", size="medium")
        drink1.add_flavor("lemon")
        food1 = Food("french fries")
        food1.add_topping("nacho cheese")
        food1.add_topping("chili")
        order.add_item(drink1)
        order.add_item(food1)
        
        expected_receipt = (
            "Receipt:\n"
            "Drink 1: Base = hill fog, Flavors = lemon, Size = medium, Cost: $1.90\n"
            "Food 1: Type = french fries, Toppings = nacho cheese, chili, Cost: $2.40\n"
            "Order Total: $4.61\n"
        )
        self.assertEqual(order.get_receipt(), expected_receipt)


if __name__ == "__main__":
    unittest.main()
