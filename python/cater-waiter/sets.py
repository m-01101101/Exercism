from collections import Counter
from typing import Set, List, Tuple
from sets_categories_data import (
    VEGAN,
    VEGETARIAN,
    KETO,
    PALEO,
    OMNIVORE,
    ALCOHOLS,
    SPECIAL_INGREDIENTS,
)


def clean_ingredients(
    dish_name: str, dish_ingredients: List[str]
) -> Tuple[str, Set[str]]:
    """

    :param dish_name: str
    :param dish_ingredients: list
    :return: tuple of (dish_name, ingredient set)

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name: str, drink_ingredients: List[str]) -> str:
    """

    :param drink_name: str
    :param drink_ingredients: list
    :return: str drink name + ("Mocktail" or "Cocktail")

    The function should return the name of the drink followed by "Mocktail" if the drink has
    no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol.
    """

    def is_nonalcoholic(drink_ingredients: List[str], alcohols: Set[str]) -> bool:
        return set(drink_ingredients).isdisjoint(alcohols)

    return (
        drink_name + " Mocktail"
        if is_nonalcoholic(drink_ingredients, ALCOHOLS)
        else drink_name + " Cocktail"
    )


def categorize_dish(dish_name: str, dish_ingredients: List[str]) -> str:
    """

    :param dish_name: str
    :param dish_ingredients: list
    :return: str "dish name: CATEGORY"

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    All dishes will "fit" into one of the categories imported from `categories.py`
    (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    """
    num_ingredients = len(set(dish_ingredients))

    def is_vegan(dish_ingredients: List[str], vegan_ingredients: Set[str]) -> bool:
        return (
            len(set(dish_ingredients).intersection(vegan_ingredients))
            == num_ingredients
        )

    def is_vege(dish_ingredients: List[str], vege_ingredients: Set[str]) -> bool:
        return (
            len(set(dish_ingredients).intersection(vege_ingredients)) == num_ingredients
        )

    def is_keto(dish_ingredients: List[str], keto_ingredients: Set[str]) -> bool:
        return (
            len(set(dish_ingredients).intersection(keto_ingredients)) == num_ingredients
        )

    def is_paleo(dish_ingredients: List[str], paleo_ingredients: Set[str]) -> bool:
        return (
            len(set(dish_ingredients).intersection(paleo_ingredients))
            == num_ingredients
        )

    def is_omnivore(
        dish_ingredients: List[str], omnivore_ingredients: Set[str]
    ) -> bool:
        return (
            len(set(dish_ingredients).intersection(omnivore_ingredients))
            == num_ingredients
        )

    if is_vegan(dish_ingredients, VEGAN):
        return dish_name + ": VEGAN"
    elif is_vege(dish_ingredients, VEGETARIAN):
        return dish_name + ": VEGETARIAN"
    elif is_keto(dish_ingredients, KETO):
        return dish_name + ": KETO"
    elif is_paleo(dish_ingredients, PALEO):
        return dish_name + ": PALEO"
    elif is_omnivore(dish_ingredients, OMNIVORE):
        return dish_name + ": OMNIVORE"
    else:
        raise ValueError("Ingredients did not match category")

    # better approach would have been:
    # categories = {
    #     "VEGAN": VEGAN,
    #     "VEGETARIAN": VEGETARIAN,
    #     "PALEO": PALEO,
    #     "KETO": KETO,
    #     "OMNIVORE": OMNIVORE,
    # }
    # for each in categories.items():
    #     if set(dish_ingredients) <= each[1]:
    #         category = each[0]

    #         break
    # return dish_name + ": " + category
    #
    # by stuartclothier


def tag_special_ingredients(dish: Tuple[str, List[str]]) -> Tuple[str, Set[str]]:
    """

    :param dish: tuple of (str of dish name, list of dish ingredients)
    :return: tuple of (str of dish name, set of dish special ingredients)

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `categories.py`.
    """

    return (dish[0], set(dish[1]).intersection(SPECIAL_INGREDIENTS))


def compile_ingredients(dishes: List[Set[str]]) -> Set[str]:
    """

    :param dishes: list of dish ingredient sets
    :return: set

    This function should return a `set` of all ingredients from all listed dishes.
    """

    return set().union(*dishes)


def separate_appetizers(dishes: List[str], appetizers: List[str]) -> List[str]:
    """

    :param dishes: list of dish names
    :param appetizers: list of appetizer names
    :return: list of dish names

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    return set(dishes).difference(appetizers)


def singleton_ingredients(dishes: List[Set[str]], intersection: Set[str]) -> Set[str]:
    """

    :param intersection: constant - one of (VEGAN_INTERSECTION,VEGETARIAN_INTERSECTION,PALEO_INTERSECTION,
                                            KETO_INTERSECTION,OMNIVORE_INTERSECTION)
    :param dishes:  list of ingredient sets
    :return: set of singleton ingredients

    Each dish is represented by a `set` of its ingredients.
    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category.
    The function should return a `set` of ingredients that only appear in a single dish.
    """
    singletons = (dish - intersection for dish in dishes)

    return set.union(*singletons)
