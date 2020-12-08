# prefix_again



**Requirements:**
```eval_rst
- :ref:`fundamentals:mathematical operations`
- :ref:`fundamentals:substrings and slicing`
- :ref:`fundamentals:loop with a counter variable`
- :ref:`fundamentals:if, else`
- :ref:`fundamentals:break`

```


Get a `string` and a prefix length `n` from the user. Does a prefix of size `n` appear somewhere else in the string? Output `True` if it does, and `False` if not. Assume that `string` is not empty and that `n` is in the range `1..len(string)`.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p136417) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
'abXYabc'
1
```
**Output:**
```
True
```
### Test 2
**Input:**
```
'abXYabc'
2
```
**Output:**
```
True
```
### Test 3
**Input:**
```
'abXYabc'
3
```
**Output:**
```
False
```
### Test 4
**Input:**
```
'xyzxyxyxy'
2
```
**Output:**
```
True
```
### Test 5
**Input:**
```
'xyzxyxyxy'
3
```
**Output:**
```
False
```
### Test 6
**Input:**
```
'Hi12345Hi6789Hi10'
1
```
**Output:**
```
True
```
### Test 7
**Input:**
```
'Hi12345Hi6789Hi10'
2
```
**Output:**
```
True
```
### Test 8
**Input:**
```
'Hi12345Hi6789Hi10'
3
```
**Output:**
```
True
```
### Test 9
**Input:**
```
'Hi12345Hi6789Hi10'
4
```
**Output:**
```
False
```
### Test 10
**Input:**
```
'a'
1
```
**Output:**
```
False
```
### Test 11
**Input:**
```
'aa'
1
```
**Output:**
```
True
```
### Test 12
**Input:**
```
'ab'
1
```
**Output:**
```
False
```

