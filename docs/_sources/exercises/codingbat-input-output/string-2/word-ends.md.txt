# word_ends




Given a string and a non-empty <b>word</b> string, return a string made of each char just before and just after every appearance of the word in the string. Ignore cases where there is no char before or after the word, and a char may be included twice if it is between two words.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p147538) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
'abcXY123XYijk'
'XY'
```
**Output:**
```
'c13i'
```
### Test 2
**Input:**
```
'XY123XY'
'XY'
```
**Output:**
```
'13'
```
### Test 3
**Input:**
```
'XY1XY'
'XY'
```
**Output:**
```
'11'
```
### Test 4
**Input:**
```
'XYXY'
'XY'
```
**Output:**
```
'XY'
```
### Test 5
**Input:**
```
'XY'
'XY'
```
**Output:**
```
''
```
### Test 6
**Input:**
```
'Hi'
'XY'
```
**Output:**
```
''
```
### Test 7
**Input:**
```
''
'XY'
```
**Output:**
```
''
```
### Test 8
**Input:**
```
'abc1xyz1i1j'
'1'
```
**Output:**
```
'cxziij'
```
### Test 9
**Input:**
```
'abc1xyz1'
'1'
```
**Output:**
```
'cxz'
```
### Test 10
**Input:**
```
'abc1xyz11'
'1'
```
**Output:**
```
'cxz11'
```
### Test 11
**Input:**
```
'abc1xyz1abc'
'abc'
```
**Output:**
```
'11'
```
### Test 12
**Input:**
```
'abc1xyz1abc'
'b'
```
**Output:**
```
'acac'
```
### Test 13
**Input:**
```
'abc1abc1abc'
'abc'
```
**Output:**
```
'1111'
```

