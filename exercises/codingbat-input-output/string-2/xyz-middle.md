# xyz_middle



**Requirements:**
```eval_rst
- :ref:`fundamentals:mathematical operations`
- :ref:`fundamentals:substrings and slicing`
- :ref:`fundamentals:loop with a counter variable`

```


Given a string, does `"xyz"` appear in the middle of the string? To define middle, we'll say that the number of chars to the left and right of the `"xyz"` must differ by at most one. This problem is harder than it looks.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p159772) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
'AAxyzBB'
```
**Output:**
```
True
```
### Test 2
**Input:**
```
'AxyzBB'
```
**Output:**
```
True
```
### Test 3
**Input:**
```
'AxyzBBB'
```
**Output:**
```
False
```
### Test 4
**Input:**
```
'AxyzBBBB'
```
**Output:**
```
False
```
### Test 5
**Input:**
```
'AAAxyzB'
```
**Output:**
```
False
```
### Test 6
**Input:**
```
'AAAxyzBB'
```
**Output:**
```
True
```
### Test 7
**Input:**
```
'AAAAxyzBB'
```
**Output:**
```
False
```
### Test 8
**Input:**
```
'AAAAAxyzBBB'
```
**Output:**
```
False
```
### Test 9
**Input:**
```
'1x345xyz12x4'
```
**Output:**
```
True
```
### Test 10
**Input:**
```
'xyzAxyzBBB'
```
**Output:**
```
True
```
### Test 11
**Input:**
```
'xyzAxyzBxyz'
```
**Output:**
```
True
```
### Test 12
**Input:**
```
'xyzxyzAxyzBxyzxyz'
```
**Output:**
```
True
```
### Test 13
**Input:**
```
'xyzxyzxyzBxyzxyz'
```
**Output:**
```
True
```
### Test 14
**Input:**
```
'xyzxyzAxyzxyzxyz'
```
**Output:**
```
True
```
### Test 15
**Input:**
```
'xyzxyzAxyzxyzxy'
```
**Output:**
```
False
```
### Test 16
**Input:**
```
'AxyzxyzBB'
```
**Output:**
```
False
```
### Test 17
**Input:**
```
''
```
**Output:**
```
False
```
### Test 18
**Input:**
```
'x'
```
**Output:**
```
False
```
### Test 19
**Input:**
```
'xy'
```
**Output:**
```
False
```
### Test 20
**Input:**
```
'xyz'
```
**Output:**
```
True
```
### Test 21
**Input:**
```
'xyzz'
```
**Output:**
```
True
```

