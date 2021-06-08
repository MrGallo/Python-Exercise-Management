# Within Range





You fix the silly error you made in the previous question and present the algorithm again to your commander. This time he is interested. He looks at the list of sorted enemies and notice the first enemy ship in the list of priority targets is beyond the ship's weapons range and that it would be useless to target that ship first. Create a filter function that will filter out enemy ships beyond weapons range (`50` units).

## Starter Code
```python
from typing import List


class Ship:
    pass


def filter_by_distance(ships: List[Ship], distance: int) -> List[Ship]:
    pass
```

## Tests
```python
from main import Ship, filter_by_distance


def test_filter_one_ship_by_distance():
    s = Ship(0, 0, 0, 0)

    assert filter_by_distance([s], 50) == [s]


def test_filter_ships_by_distance():

    s1 = Ship(1, 0, 0)
    s2 = Ship(2, 0, 0)
    s3 = Ship(3, 0, 0)

    ships = [s1, s2, s3]
    assert filter_by_distance(ships, 2) == [s1, s2]
```
