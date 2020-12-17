# All Construct





You can learn more from Free Code Camp's [Dynamic Programming](https://www.youtube.com/watch?v=oBt53YbR9Kk) video.

## Starter Code
```python
from typing import List


def all_construct(target: str, wordbank: List[str]) -> List[List[str]]:
    pass
```

## Tests
```python
from main import all_construct


def test_count_construct_base_case():
    assert all_construct("", []) == [[]]


def test_count_construct():
    assert all_construct("hi", []) == None
    assert all_construct("skateboard", "bo rd ate t ska sk boar".split()) == None
    assert len(all_construct("purple", "purp p ur le purpl".split())) == 2
    assert len(all_construct("abcdef", "ab abc cd def abcd ef c".split())) == 4
    assert len(all_construct("enterapotentpot", "a p ent enter ot o t".split())) == 4


def test_count_construct_memo():
    assert all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                         "e ee eee eeee eeeee eeeeee eeeeeee".split()) == None
```
