# end_other



**Requirements:**
```eval_rst
- :ref:`fundamentals:substrings and slicing`
- :ref:`fundamentals:if, elif, else`

```


Take two strings as input, output `True` if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Output `False` otherwise. Note: `str.lower()` returns the lowercase version of a string.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p126880) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
'Hiabc'
'abc'
```
**Output:**
```
True
```
### Test 2
**Input:**
```
'AbC'
'HiaBc'
```
**Output:**
```
True
```
### Test 3
**Input:**
```
'abc'
'abXabc'
```
**Output:**
```
True
```
### Test 4
**Input:**
```
'Hiabc'
'abcd'
```
**Output:**
```
False
```
### Test 5
**Input:**
```
'Hiabc'
'bc'
```
**Output:**
```
True
```
### Test 6
**Input:**
```
'Hiabcx'
'bc'
```
**Output:**
```
False
```
### Test 7
**Input:**
```
'abc'
'abc'
```
**Output:**
```
True
```
### Test 8
**Input:**
```
'xyz'
'12xyz'
```
**Output:**
```
True
```
### Test 9
**Input:**
```
'yz'
'12xz'
```
**Output:**
```
False
```
### Test 10
**Input:**
```
'Z'
'12xz'
```
**Output:**
```
True
```
### Test 11
**Input:**
```
'12'
'12'
```
**Output:**
```
True
```
### Test 12
**Input:**
```
'abcXYZ'
'abcDEF'
```
**Output:**
```
False
```
### Test 13
**Input:**
```
'ab'
'ab12'
```
**Output:**
```
False
```
### Test 14
**Input:**
```
'ab'
'12ab'
```
**Output:**
```
True
```

