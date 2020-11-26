# count_code




Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p123614) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






## Tests
### Test 1
**Input:**
```
'aaacodebbb'
```
**Output:**
```
1
```
### Test 2
**Input:**
```
'codexxcode'
```
**Output:**
```
2
```
### Test 3
**Input:**
```
'cozexxcope'
```
**Output:**
```
2
```
### Test 4
**Input:**
```
'cozfxxcope'
```
**Output:**
```
1
```
### Test 5
**Input:**
```
'xxcozeyycop'
```
**Output:**
```
1
```
### Test 6
**Input:**
```
'cozcop'
```
**Output:**
```
0
```
### Test 7
**Input:**
```
'abcxyz'
```
**Output:**
```
0
```
### Test 8
**Input:**
```
'code'
```
**Output:**
```
1
```
### Test 9
**Input:**
```
'ode'
```
**Output:**
```
0
```
### Test 10
**Input:**
```
'c'
```
**Output:**
```
0
```
### Test 11
**Input:**
```
''
```
**Output:**
```
0
```
### Test 12
**Input:**
```
'AAcodeBBcoleCCccoreDD'
```
**Output:**
```
3
```
### Test 13
**Input:**
```
'AAcodeBBcoleCCccorfDD'
```
**Output:**
```
2
```
### Test 14
**Input:**
```
'coAcodeBcoleccoreDD'
```
**Output:**
```
3
```

