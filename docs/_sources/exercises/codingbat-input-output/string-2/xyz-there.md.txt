# xyz_there




Return true if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p136594) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
'abcxyz'
```
**Output:**
```
True
```
### Test 2
**Input:**
```
'abc.xyz'
```
**Output:**
```
False
```
### Test 3
**Input:**
```
'xyz.abc'
```
**Output:**
```
True
```
### Test 4
**Input:**
```
'abcxy'
```
**Output:**
```
False
```
### Test 5
**Input:**
```
'xyz'
```
**Output:**
```
True
```
### Test 6
**Input:**
```
'xy'
```
**Output:**
```
False
```
### Test 7
**Input:**
```
'x'
```
**Output:**
```
False
```
### Test 8
**Input:**
```
''
```
**Output:**
```
False
```
### Test 9
**Input:**
```
'abc.xyzxyz'
```
**Output:**
```
True
```
### Test 10
**Input:**
```
'abc.xxyz'
```
**Output:**
```
True
```
### Test 11
**Input:**
```
'.xyz'
```
**Output:**
```
False
```
### Test 12
**Input:**
```
'12.xyz'
```
**Output:**
```
False
```
### Test 13
**Input:**
```
'12xyz'
```
**Output:**
```
True
```
### Test 14
**Input:**
```
'1.xyz.xyz2.xyz'
```
**Output:**
```
False
```

