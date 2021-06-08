# Enemy Ship Distance





You are the sensors officer on a spaceship in enemy territory. You notice an incoming enemy fleet coming to attack you. Your commander is overwhelmed with which enemy vessel to attack first. You decide it might be helpful to attack the closest enemies first, so naturally, you decide to create a bubble-sort algorithm so you can hand off the sorted list to the weapons officer. All the enemy ships have an `x`, `y`, and `z` comonent, which is the distance from them to your current location. For some strange reason, they are all converging from the same plane making the `z` component irrevelant. (It's almost like they exist in a top-down space-shooter game, weird). Create a function that will sort a list of enemies based on their relative distances, their `(x, y)` co-ordinates. The function will take a list of `Ship` objects and return a new list sorted.

## Starter Code
```python
from typing import List


class Ship:
    pass


def sort_by_distance(ships: List[Ship]) -> List[Ship]:
    pass
```

## Tests
```python
from main import sort_by_distance, Ship
import random


def test_sort_single_ship_by_distance():
    ship = Ship(3, 4, 0)
    assert sort_by_distance([ship]) == [ship]


def test_sort_two_ships_by_distance():
    ship1 = Ship(1, 1, 0)
    ship2 = Ship(5, 5, 0)

    original = [ship2, ship1]
    result = sort_by_distance(original)
    expected = [ship1, ship2]
    assert result == expected

def test_acceptance():
    original = []
    for x in range(100):
        s = Ship(x, 0, 0)
        original.append(s)  
    
    unsorted = random.sample(original, len(original))

    result = sort_by_distance(unsorted)
    assert result == original
```
