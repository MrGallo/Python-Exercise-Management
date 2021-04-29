# Shopping List



**Requirements:**
```eval_rst
- :ref:`fundamentals:defining a function`
- :ref:`fundamentals:defining parameters`
- :ref:`fundamentals:iterating through dictionary keys and values`
- :ref:`fundamentals:accessing a value in a dictionary`
- :ref:`fundamentals:list building and filtering`
- :ref:`fundamentals:returning a value`

```


From scratch, code the function as described below:

```
get_shopping_list(inventory: Dict[str, int], minimum_stock: Dict[str, int]) -> List[str]
```

This function will take an inventory dictionary and a dictionary of minimum stock associated with each item in the fridge.

The function will determine if we need to purchase more of any  particular item based on its current inventory value and its minimum stock value.

```
inventory = {
    "apples": 5,
    "oranges": 5
}

minimum_stock = {
    "apples": 10,
    "oranges": 5
}
```

As shown in the example above, the current inventory value of apples is `5`. Apples have a minimum stock level of `10`, therefore, we need to order more apples.

Our inventory level of oranges is `5`, but the minimum allowed stock is `5`, so we *do not* have to buy more oranges.

Therefore the shopping list for this particular scenario will be:

```
["apples"]
```

All we need is a list of items to buy, not how many of each to buy. *Note:* for the sake of simplicity, you can assume
both dictionaries contain the exact same keys.






## Tests
```python
from main import get_shopping_list


def test_get_shopping_list_example():
    inventory = {
        "apples": 5,
        "oranges": 5
    }

    min_stock_allowed = {
        "apples": 10,
        "oranges": 5
    }

    assert get_shopping_list(inventory, min_stock_allowed) == ["apples"]


def test_get_shopping_list_empty():
    inventory = {
        "apples": 25,
        "oranges": 50
    }

    min_stock_allowed = {
        "apples": 10,
        "oranges": 5
    }

    assert get_shopping_list(inventory, min_stock_allowed) == []


def test_get_shopping_list_empty():
    inventory = {
        "apples": 25,
        "oranges": 50,
        "bananas": 32,
        "propane": 3,
        "fire": 11
    }

    min_stock_allowed = {
        "apples": 27,
        "oranges": 50,
        "bananas": 52,
        "propane": 7,
        "fire": 5
    }

    assert get_shopping_list(inventory, min_stock_allowed) == ["apples", "bananas", "propane"]
```
