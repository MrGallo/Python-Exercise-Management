# Can Construct





Write a function `can_construct(target, wordbank)` that accepts a target string and a list of strings.

The function should return a boolean indicating whether or not the `target` can be constructed by concatenating elements of the `wordbank` list.

You may reuse elements of `wordbank` as many times as needed.

You can learn more from Free Code Camp's [Dynamic Programming](https://www.youtube.com/watch?v=oBt53YbR9Kk) video.

## Starter Code
```python
from typing import List


def can_construct(target: str, wordbank: List[str]) -> bool:
    pass
```

## Tests
```python
from main import can_construct


def test_can_construct_base_case():
    assert can_construct("", []) == True

def test_can_construct():
    assert can_construct("abcdef", "ab abc cd def abcd".split()) == True
    assert can_construct("skateboard", "bo rd ate t ska sk boar".split()) == False
    assert can_construct("enterapotentpot", "a p ent enter ot o t".split()) == True


def test_can_construct_memo():
    assert can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                         "e ee eee eeee eeeee eeeeee eeeeeee eeeeeeee".split()) == False
```
