# ten_run





For each multiple of 10 in the given list, change all the values following it to be that multiple of 10, until encountering another multiple of 10. So {2, 10, 3, 4, 20, 5} yields {2, 10, 10, 10, 20, 20}.

```
ten_run([2, 10, 3, 4, 20, 5]) -> [2, 10, 10, 10, 20, 20]
ten_run([10, 1, 20, 2]) -> [10, 10, 20, 20]
ten_run([10, 1, 9, 20]) -> [10, 10, 10, 20]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p199484) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def ten_run(nums: List[int]) -> List[int]:
    pass


result = ten_run([2, 10, 3, 4, 20, 5])
print(result)
```

## Tests
```python
from main import ten_run


def test_ten_run_1():
    assert ten_run([2, 10, 3, 4, 20, 5]) == [2, 10, 10, 10, 20, 20]


def test_ten_run_2():
    assert ten_run([10, 1, 20, 2]) == [10, 10, 20, 20]


def test_ten_run_3():
    assert ten_run([10, 1, 9, 20]) == [10, 10, 10, 20]


def test_ten_run_4():
    assert ten_run([1, 2, 50, 1]) == [1, 2, 50, 50]


def test_ten_run_5():
    assert ten_run([1, 20, 50, 1]) == [1, 20, 50, 50]


def test_ten_run_6():
    assert ten_run([10, 10]) == [10, 10]


def test_ten_run_7():
    assert ten_run([10, 2]) == [10, 10]


def test_ten_run_8():
    assert ten_run([0, 2]) == [0, 0]


def test_ten_run_9():
    assert ten_run([1, 2]) == [1, 2]


def test_ten_run_10():
    assert ten_run([1]) == [1]


def test_ten_run_11():
    assert ten_run([]) == []
```
