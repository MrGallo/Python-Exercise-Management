# two_char





Given a string and an index, return a string length 2 starting at the given index. If the index is too big or too small to define a string length 2, use the first 2 chars. The string length will be at least 2.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p144623) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
'java'
0
```
**Output:**
```
'ja'
```
### Test 2
**Input:**
```
'java'
2
```
**Output:**
```
'va'
```
### Test 3
**Input:**
```
'java'
3
```
**Output:**
```
'ja'
```
### Test 4
**Input:**
```
'java'
4
```
**Output:**
```
'ja'
```
### Test 5
**Input:**
```
'java'
-1
```
**Output:**
```
'ja'
```
### Test 6
**Input:**
```
'Hello'
0
```
**Output:**
```
'He'
```
### Test 7
**Input:**
```
'Hello'
1
```
**Output:**
```
'el'
```
### Test 8
**Input:**
```
'Hello'
99
```
**Output:**
```
'He'
```
### Test 9
**Input:**
```
'Hello'
3
```
**Output:**
```
'lo'
```
### Test 10
**Input:**
```
'Hello'
4
```
**Output:**
```
'He'
```
### Test 11
**Input:**
```
'Hello'
5
```
**Output:**
```
'He'
```
### Test 12
**Input:**
```
'Hello'
-7
```
**Output:**
```
'He'
```
### Test 13
**Input:**
```
'Hello'
6
```
**Output:**
```
'He'
```
### Test 14
**Input:**
```
'Hello'
-1
```
**Output:**
```
'He'
```
### Test 15
**Input:**
```
'yay'
0
```
**Output:**
```
'ya'
```

