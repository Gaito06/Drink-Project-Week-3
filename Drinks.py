from typing import List

class Drink:
    """
    A class to represent a drink with a base and a list of flavors.
    
    Attributes:
        base (str): The base of the drink (e.g., 'water', 'sbrite').
        flavors (List[str]): A list of added flavors to the drink.
    
    Methods:
        get_base: Returns the base of the drink.
        get_flavors: Returns the list of flavors in the drink.
        add_flavor: Adds a flavor to the drink if it is valid.
        set_flavors: Sets a list of flavors for the drink.
        get_total: Returns the total cost of the drink based on size and flavors.
        set_size: Allows changing the size of the drink.
    """
    
    # List of possible valid bases and flavors (these don't change)
    _valid_bases = ["water", "sbrite", "pokeacola", "Mr. Salt", "hill fog", "leaf wine"]
    _valid_flavors = ["lemon", "cherry", "strawberry", "mint", "blueberry", "lime"]
    
    # List of possible sizes and their associated prices
    _size_prices = {
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "mega": 2.15
    }
    
    def __init__(self, base: str, size: str):
        """
        Initializes the drink with a base and size.
        
        Args:
            base (str): The base of the drink (e.g., 'water', 'sbrite').
            size (str): The size of the drink (e.g., 'small', 'medium', 'large', 'mega').
        
        Raises:
            ValueError: If the base or size is invalid.
        """
        # Set base if it's valid, else raise an exception
        if base.lower() in Drink._valid_bases:
            self._base = base.lower()  # Store base in lowercase
        else:
            raise ValueError("Invalid base")
        
        # Set size if it's valid, else raise an exception
        if size.lower() in Drink._size_prices:
            self._size = size.lower()  # Store size in lowercase
        else:
            raise ValueError("Invalid size")
        
        # Initialize flavors as an empty list
        self._flavors = []

    def get_base(self) -> str:
        """
        Returns the base of the drink.
        
        Returns:
            str: The base of the drink.
        """
        return self._base

    def get_flavors(self) -> List[str]:
        """
        Returns the list of flavors in the drink.
        
        Returns:
            List[str]: List of flavors added to the drink.
        """
        return self._flavors

    def add_flavor(self, flavor: str):
        """
        Adds a valid flavor to the drink.
        
        Args:
            flavor (str): The flavor to be added to the drink.
        
        Raises:
            ValueError: If the flavor is invalid or already added.
        """
        # Check if the flavor is valid
        if flavor.lower() not in Drink._valid_flavors:
            raise ValueError(f"Invalid flavor: {flavor}")
        
        # Add the flavor if it's not already in the list
        if flavor.lower() not in self._flavors:
            self._flavors.append(flavor.lower())
        else:
            print(f"Flavor '{flavor}' is already added.")

    def set_flavors(self, flavors: List[str]):
        """
        Sets the list of flavors for the drink, replacing any existing ones.
        
        Args:
            flavors (List[str]): A list of flavors to set for the drink.
        
        Raises:
            ValueError: If any flavor is invalid.
        """
        # Ensure all flavors are valid
        for flavor in flavors:
            if flavor.lower() not in Drink._valid_flavors:
                raise ValueError(f"Invalid flavor: {flavor}")
        
        # Remove duplicates by converting to a set and store the list of flavors
        self._flavors = list(set(flavors))

    def get_total(self) -> float:
        """
        Calculates the total cost of the drink based on its size and added flavors.
        
        Returns:
            float: The total cost of the drink.
        """
        # Start with the base price for the drink size
        total_cost = Drink._size_prices[self._size]
        
        # Add $0.15 for each added flavor
        total_cost += 0.15 * len(self._flavors)
        
        return total_cost

    def set_size(self, size: str):
        """
        Sets a new size for the drink.
        
        Args:
            size (str): The new size for the drink (e.g., 'small', 'medium', 'large', 'mega').
        
        Raises:
            ValueError: If the size is invalid.
        """
        # Set size if it's valid, else raise an exception
        if size.lower() in Drink._size_prices:
            self._size = size.lower()
        else:
            raise ValueError("Invalid size")


class Food:
    """
    A class to represent a food item with toppings and its associated cost.
    
    Attributes:
        food_type (str): The type of food (e.g., 'hotdog', 'french fries').
        toppings (List[str]): A list of toppings added to the food.
    
    Methods:
        get_food_type: Returns the type of the food.
        add_topping: Adds a topping to the food.
        get_toppings: Returns the list of toppings added to the food.
        get_price: Returns the price of the base food item.
        get_total: Returns the total cost of the food, including toppings.
        get_topping_count: Returns the number of toppings added to the food.
    """
    
    # Dictionary of food types with their base prices
    _food_prices = {
        "hotdog": 2.30,
        "corndog": 2.00,
        "ice cream": 3.00,
        "onion rings": 1.75,
        "french fries": 1.50,
        "tater tots": 1.70,
        "nacho chips": 1.90
    }
    
    # List of valid toppings and their prices
    _valid_toppings = {
        "cherry": 0.00,
        "whipped cream": 0.00,
        "caramel sauce": 0.50,
        "chocolate sauce": 0.50,
        "nacho cheese": 0.30,
        "chili": 0.60,
        "bacon bits": 0.30,
        "ketchup": 0.00,
        "mustard": 0.00
    }
    
    def __init__(self, food_type: str):
        """
        Initializes the food item with a type and an empty list of toppings.
        
        Args:
            food_type (str): The type of food (e.g., 'hotdog', 'french fries').
        
        Raises:
            ValueError: If the food type is invalid.
        """
        # Set the food type if it's valid, else raise an exception
        if food_type.lower() in Food._food_prices:
            self.food_type = food_type.lower()
        else:
            raise ValueError(f"Invalid food type: {food_type}")
        
        # Initialize toppings as an empty list
        self.toppings = []

    def get_food_type(self) -> str:
        """
        Returns the type of the food.
        
        Returns:
            str: The type of the food item (e.g., 'hotdog', 'french fries').
        """
        return self.food_type

    def add_topping(self, topping: str):
        """
        Adds a valid topping to the food.
        
        Args:
            topping (str): The topping to be added to the food.
        
        Raises:
            ValueError: If the topping is invalid.
        """
        # Check if the topping is valid
        if topping.lower() not in Food._valid_toppings:
            raise ValueError(f"Invalid topping: {topping}")
        
        # Add the topping if it's not already in the list
        if topping.lower() not in self.toppings:
            self.toppings.append(topping.lower())
        else:
            print(f"Topping '{topping}' is already added.")

    def get_toppings(self) -> List[str]:
        """
        Returns the list of toppings added to the food.
        
        Returns:
            List[str]: The list of toppings added to the food.
        """
        return self.toppings

    def get_price(self) -> float:
        """
        Returns the price of the base food item (without toppings).
        
        Returns:
            float: The base price of the food item.
        """
        return Food._food_prices[self.food_type]

    def get_total(self) -> float:
        """
        Calculates the total cost of the food, including the base price and toppings.
        
        Returns:
            float: The total cost of the food.
        """
        total_cost = Food._food_prices[self.food_type]
        
        # Add the cost of each topping
        for topping in self.toppings:
            total_cost += Food._valid_toppings[topping]
        
        return total_cost

    def get_topping_count(self) -> int:
        """
        Returns the number of toppings added to the food.
        
        Returns:
            int: The number of toppings added to the food.
        """
        return len(self.toppings)


class Order:
    """
    A class to represent an order containing multiple drinks and food items.
    
    Attributes:
        items (List[Union[Drink, Food]]): A list of items (drinks and food) in the order.
    
    Methods:
        add_item: Adds a drink or food item to the order.
        get_items: Returns the list of items in the order.
        get_total: Returns the total cost of the order, including tax.
        get_receipt: Returns a string summary of the order.
    """
    
    def __init__(self):
        """
        Initializes the order with an empty list of items (drinks and food).
        """
        self._items = []

    def add_item(self, item: 'Union[Drink, Food]'):
        """
        Adds a drink or food item to the order.
        
        Args:
            item (Union[Drink, Food]): The drink or food item to add to the order.
        """
        self._items.append(item)

    def get_items(self) -> List['Union[Drink, Food]']:
        """
        Returns the list of items in the order.
        
        Returns:
            List[Union[Drink, Food]]: The list of drinks and food items in the order.
        """
        return self._items

    def get_total(self) -> float:
        """
        Calculates the total cost of the order, including tax.
        
        Returns:
            float: The total cost of the order with tax.
        """
        # Calculate the total cost of all items
        total_cost = sum(item.get_total() for item in self._items)
        
        # Apply a 7.25% tax to the total
        total_with_tax = total_cost * 1.0725
        return total_with_tax

    def get_receipt(self) -> str:
        """
        Generates a receipt for the order, including all items and their costs.
        
        Returns:
            str: The formatted receipt for the order.
        """
        receipt = "Receipt:\n"
        
        for index, item in enumerate(self._items, 1):
            if isinstance(item, Drink):
                receipt += (f"Drink {index}: Base = {item.get_base()}, "
                            f"Flavors = {', '.join(item.get_flavors())}, "
                            f"Size = {item.get_size()}, Cost: ${item.get_total():.2f}\n")
            elif isinstance(item, Food):
                receipt += (f"Food {index}: Type = {item.get_food_type()}, "
                            f"Toppings = {', '.join(item.get_toppings())}, "
                            f"Cost: ${item.get_total():.2f}\n")
        
        receipt += f"Order Total: ${self.get_total():.2f}\n"
        return receipt
