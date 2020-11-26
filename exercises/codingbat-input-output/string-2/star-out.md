# star_out




Return a version of the given string, where for every star (*) in the string the star and the chars immediately to its left and right are gone. So "ab*cd" yields "ad" and "ab**cd" also yields "ad".

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p139564) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






## Tests
### Test 1
**Input:**
```
'ab*cd'
```
**Output:**
```
'ad'
```
### Test 2
**Input:**
```
'ab**cd'
```
**Output:**
```
'ad'
```
### Test 3
**Input:**
```
'sm*eilly'
```
**Output:**
```
'silly'
```
### Test 4
**Input:**
```
'sm*eil*ly'
```
**Output:**
```
'siy'
```
### Test 5
**Input:**
```
'sm**eil*ly'
```
**Output:**
```
'siy'
```
### Test 6
**Input:**
```
'sm***eil*ly'
```
**Output:**
```
'siy'
```
### Test 7
**Input:**
```
'stringy*'
```
**Output:**
```
'string'
```
### Test 8
**Input:**
```
'*stringy'
```
**Output:**
```
'tringy'
```
### Test 9
**Input:**
```
'*str*in*gy'
```
**Output:**
```
'ty'
```
### Test 10
**Input:**
```
'abc'
```
**Output:**
```
'abc'
```
### Test 11
**Input:**
```
'a*bc'
```
**Output:**
```
'c'
```
### Test 12
**Input:**
```
'ab'
```
**Output:**
```
'ab'
```
### Test 13
**Input:**
```
'a*b'
```
**Output:**
```
''
```
### Test 14
**Input:**
```
'a'
```
**Output:**
```
'a'
```
### Test 15
**Input:**
```
'a*'
```
**Output:**
```
''
```
### Test 16
**Input:**
```
'*a'
```
**Output:**
```
''
```
### Test 17
**Input:**
```
'*'
```
**Output:**
```
''
```
### Test 18
**Input:**
```
''
```
**Output:**
```
''
```

