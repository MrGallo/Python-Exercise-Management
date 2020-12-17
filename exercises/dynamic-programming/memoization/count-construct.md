# Count Construct





Write a function `count_construct(target, wordbank)` that accepts a target string and an array of strings.

The function should return the number of ways that the `target` can be constructed by concatenating elements of the `wordbank` list.

You may reuse elements of `wordbank` as many times as needed.

You can learn more from Free Code Camp's [Dynamic Programming](https://www.youtube.com/watch?v=oBt53YbR9Kk) video.

## Starter Code
```python
from typing import List


def count_construct(target: str, wordbank: List[str]) -> int:
    pass
```

## Tests
```python
from main import count_construct


def test_count_construct_base_case():
    assert count_construct("", []) == 1


def test_count_construct():
    assert count_construct("hi", []) == 0
    assert count_construct("purple", "purp p ur le purpl".split()) == 2
    assert count_construct("abcdef", "ab abc cd def abcd ef c".split()) == 4
    assert count_construct("skateboard", "bo rd ate t ska sk boar".split()) == 0
    assert count_construct("enterapotentpot", "a p ent enter ot o t".split()) == 4


def test_count_construct_memo():
    assert count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                           "e ee eee eeee eeeee eeeeee eeeeeee".split()) == 0
```
