from typing import Dict, List


class Smoothie:
    def __init__(self, ingredients: Dict[str, float]) -> None:
        self.ingredients = ingredients

    def get_cost(self) -> float:
        """method which calculates the total cost of the ingredients used to make the smoothie."""
        cost = 0
        for item in self.ingredients:
            cost += product_list.get(item)
        return cost

    def get_price(self) -> float:
        """method which returns the number from get_cost plus the number from get_cost multiplied by 1.5."""
        price = self.get_cost()
        price = price + price * 1.5
        return price

    def get_name(self) -> List[str]:
        """method which gets the ingredients and puts them in alphabetical order"""
        order_list = []
        for item in self.ingredients:
            order_list.append(item)
        order_list = sorted(order_list, reverse=False)
        order_list = ' '.join(order_list)
        return order_list


class BananaSmothie(Smoothie):
    """Making banana smothie from banana, full-fat milk"""

    def __init__(self) -> None:
        banana_smothie_ingredients = {'banana', 'full-fat milk'}
        super().__init__(ingredients=banana_smothie_ingredients)


class AppleSmothie(Smoothie):
    """Making apple smothie from honey, milk, banana"""

    def __init__(self) -> None:
        apple_smothie_ingredients = {'honey', 'milk', 'banana'}
        super().__init__(ingredients=apple_smothie_ingredients)


if __name__ == "__main__":
    product_list = {'banana': 1, 'blueberries': 2, 'natural yogurt': 1.99,
                    'full-fat milk': 3, 'honey': 0.59, 'milk': 3.90, }

    banana_smothie = BananaSmothie()
    apple_smothie = AppleSmothie()

    print("-"*60)
    print(f"Self cost: {banana_smothie.get_cost()}")
    print(f"Price for sale: {banana_smothie.get_price()}")
    print(f"Smothie ingredients: {banana_smothie.get_name()}")
    print("-"*60)
    print(f"Self cost: {apple_smothie.get_cost()}")
    print(f"Price for sale: {apple_smothie.get_price()}")
    print(f"Smothie ingredients: {apple_smothie.get_name()}")
    print("-"*60)
