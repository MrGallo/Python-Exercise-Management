# combo_string





Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p168564) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
'Hello'
'hi'
```
**Output:**
```
'hiHellohi'
```
### Test 2
**Input:**
```
'hi'
'Hello'
```
**Output:**
```
'hiHellohi'
```
### Test 3
**Input:**
```
'aaa'
'b'
```
**Output:**
```
'baaab'
```
### Test 4
**Input:**
```
'b'
'aaa'
```
**Output:**
```
'baaab'
```
### Test 5
**Input:**
```
'aaa'
''
```
**Output:**
```
'aaa'
```
### Test 6
**Input:**
```
''
'bb'
```
**Output:**
```
'bb'
```
### Test 7
**Input:**
```
'aaa'
'1234'
```
**Output:**
```
'aaa1234aaa'
```
### Test 8
**Input:**
```
'aaa'
'bb'
```
**Output:**
```
'bbaaabb'
```
### Test 9
**Input:**
```
'a'
'bb'
```
**Output:**
```
'abba'
```
### Test 10
**Input:**
```
'bb'
'a'
```
**Output:**
```
'abba'
```
### Test 11
**Input:**
```
'xyz'
'ab'
```
**Output:**
```
'abxyzab'
```

