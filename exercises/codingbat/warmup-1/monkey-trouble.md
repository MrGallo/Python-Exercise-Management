# monkey_trouble





We have two monkeys, a and b, and the parameters aSmile and bSmile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return true if we are in trouble.

```
monkey_trouble(true, true) â†’ true
monkey_trouble(false, false) â†’ true
monkey_trouble(true, false) â†’ false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p181646) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def monkey_trouble(a_smile: bool, b_smile: bool) -> bool:
    pass


result = monkey_trouble(True, True)
print(result)
```

## Tests
```python
from main import monkey_trouble


def test_monkey_trouble_1():
    assert monkey_trouble(True, True) == True


def test_monkey_trouble_2():
    assert monkey_trouble(False, False) == True


def test_monkey_trouble_3():
    assert monkey_trouble(True, False) == False


def test_monkey_trouble_4():
    assert monkey_trouble(False, True) == False
```
