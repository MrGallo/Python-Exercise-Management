# Highest Threat Within Range





Use the funtions created in the other parts to give the weapons officer a list of `Ship` objects within weapons range sorted by their threat-level from highest to lowest. **Note:** Be sure to *use* the previous functions you created, you don't need to re-code them in this new function.

## Starter Code
```python
from typing import List


class Ship:
    pass

def sort_by_threat(enemies: List[Ship]) -> List[Ship]:
    pass


def filter_by_distance(ships: List[Ship], distance: int) -> List[Ship]:
    pass


def sort_by_highest_threat_within_weapons_range(enemies: List[Ship], weapons_range: int) -> List[Ship]:
    pass
```

## Tests
```python
from main import Ship, sort_by_highest_threat_within_weapons_range


def test_sort_by_highest_threat_within_weapons_range():
    # within range
    s1 = Ship(1, 0, 0, firepower = 5)
    s2 = Ship(1, 0, 0, firepower = 6)  # higher threat

    s5 = Ship(5, 0, 0, firepower = 50) # highest threat within range

    s3 = Ship(5, 0, 0, firepower = 0)  # no threat (last)

    # out of range, but massive
    s4 = Ship(31, 41, 0, firepower=9000)


    all_enemies = [s1, s2, s3, s4, s5]
    expected = [s5, s2, s1, s3]  # s5 is out of range, not included

    result = sort_by_highest_threat_within_weapons_range(all_enemies, 50)
    assert result == expected
```
