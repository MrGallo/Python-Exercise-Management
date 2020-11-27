# zip_zap





Look for patterns like "zip" and "zap" in the string -- length-3, starting with 'z' and ending with 'p'. Return a string where for all such words, the middle letter is gone, so "zipXzap" yields "zpXzp".

```
zip_zap("zipXzap") â†’ "zpXzp"
zip_zap("zopzop") â†’ "zpzp"
zip_zap("zzzopzop") â†’ "zzzpzp"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p180759) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def zip_zap(string: str) -> str:
    pass


result = zip_zap('zipXzap')
print(result)
```

## Tests
```python
from main import zip_zap


def test_zip_zap_1():
    assert zip_zap('zipXzap') == 'zpXzp'


def test_zip_zap_2():
    assert zip_zap('zopzop') == 'zpzp'


def test_zip_zap_3():
    assert zip_zap('zzzopzop') == 'zzzpzp'


def test_zip_zap_4():
    assert zip_zap('zibzap') == 'zibzp'


def test_zip_zap_5():
    assert zip_zap('zip') == 'zp'


def test_zip_zap_6():
    assert zip_zap('zi') == 'zi'


def test_zip_zap_7():
    assert zip_zap('z') == 'z'


def test_zip_zap_8():
    assert zip_zap('') == ''


def test_zip_zap_9():
    assert zip_zap('zzp') == 'zp'


def test_zip_zap_10():
    assert zip_zap('abcppp') == 'abcppp'


def test_zip_zap_11():
    assert zip_zap('azbcppp') == 'azbcppp'


def test_zip_zap_12():
    assert zip_zap('azbcpzpp') == 'azbcpzp'
```
