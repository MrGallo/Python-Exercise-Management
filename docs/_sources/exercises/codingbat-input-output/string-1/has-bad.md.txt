# has_bad




Given a string, return true if "bad" appears starting at index 0 or 1 in the string, such as with "badxxx" or "xbadxx" but not "xxbadxx". The string may be any length, including 0. Note: use .equals() to compare 2 strings.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p139075) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






## Tests
### Test 1
**Input:**
```
'badxx'
```
**Output:**
```
True
```
### Test 2
**Input:**
```
'xbadxx'
```
**Output:**
```
True
```
### Test 3
**Input:**
```
'xxbadxx'
```
**Output:**
```
False
```
### Test 4
**Input:**
```
'code'
```
**Output:**
```
False
```
### Test 5
**Input:**
```
'bad'
```
**Output:**
```
True
```
### Test 6
**Input:**
```
'ba'
```
**Output:**
```
False
```
### Test 7
**Input:**
```
'xba'
```
**Output:**
```
False
```
### Test 8
**Input:**
```
'xbad'
```
**Output:**
```
True
```
### Test 9
**Input:**
```
''
```
**Output:**
```
False
```
### Test 10
**Input:**
```
'badyy'
```
**Output:**
```
True
```

