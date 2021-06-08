# Threat Level





When you finish, you tell your commander about the awesome algorithm you created. He scoffs and sarcastically reminds you that not all ships have the same fire-power and you would be wasting your time targeting smaller craft with smaller firepower. He laughs out loud at the fact that you don't even remember the simple enemy-ship-threat-calculation every cadet learns their first day at the academy (it's `firepower * 3 / distance`). Create a function to calculate a single-ship's threat. It will take a `Ship` object and consider it's `x`, `y`, and `firepower` properties.

Create a method in the `Ship` class called `.calc_threat_level()` for convenience.

## Starter Code
```python
class Ship:
    # ...
    def calc_threat_level(self) -> float:
        pass


def sort_by_threat(enemies: List[Ship]) -> List[Ship]:
    pass
```

## Tests
```python
import random

from main import Ship, sort_by_threat


def test_sort_by_threat_one_ship():
    ships = [
        Ship(0, 0, 0, 0)
    ]

    assert sort_by_threat(ships) == ships


def test_sort_by_threat_two_ships():
    ship1 = Ship(1, 1, 0, firepower=5)  # closer! More threat. Should appear first!!!
    ship2 = Ship(1, 2, 0, firepower=5)  # farther, less threat.

    assert sort_by_threat([ship2, ship1]) == [ship1, ship2]


def test_acceptance():
    sorted_ships = []
    for fp in range(100):
        s = Ship(1, 1, 0, firepower=fp)
        sorted_ships.append(s)
    sorted_ships.reverse()  # highest threat to lowest
    
    unsorted = sorted_ships[:]  # copy ship list
    random.shuffle(unsorted)  # shuffle it up

    result = sort_by_threat(unsorted)
    assert result == sorted_ships
```
