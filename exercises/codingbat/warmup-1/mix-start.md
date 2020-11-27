# mix_start





Return true if the given string begins with "mix", except the 'm' can be anything, so "pix", "9ix" .. all count.

```
mix_start("mix snacks") â†’ true
mix_start("pix snacks") â†’ true
mix_start("piz snacks") â†’ false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p151713) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def mix_start(string: str) -> bool:
    pass


result = mix_start('mix snacks')
print(result)
```

## Tests
```python
from main import mix_start


def test_mix_start_1():
    assert mix_start('mix snacks') == True


def test_mix_start_2():
    assert mix_start('pix snacks') == True


def test_mix_start_3():
    assert mix_start('piz snacks') == False


def test_mix_start_4():
    assert mix_start('nix') == True


def test_mix_start_5():
    assert mix_start('ni') == False


def test_mix_start_6():
    assert mix_start('n') == False


def test_mix_start_7():
    assert mix_start('') == False
```
