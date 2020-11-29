# mix_string



**Requirements:**
```eval_rst
- :ref:`fundamentals:get a single character`
- :ref:`fundamentals:substrings and slicing`
- :ref:`fundamentals:string building and filtering`

```


Get two strings from user input. Let's call them `a` and `b`. Create a bigger string made of the first char of `a`, the first char of `b`, the second char of `a`, the second char of `b`, and so on. Any leftover chars go at the end of the result.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p125185) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
'abc'
'xyz'
```
**Output:**
```
'axbycz'
```
### Test 2
**Input:**
```
'Hi'
'There'
```
**Output:**
```
'HTihere'
```
### Test 3
**Input:**
```
'xxxx'
'There'
```
**Output:**
```
'xTxhxexre'
```
### Test 4
**Input:**
```
'xxx'
'X'
```
**Output:**
```
'xXxx'
```
### Test 5
**Input:**
```
'2/'
'27 around'
```
**Output:**
```
'22/7 around'
```
### Test 6
**Input:**
```
''
'Hello'
```
**Output:**
```
'Hello'
```
### Test 7
**Input:**
```
'Abc'
''
```
**Output:**
```
'Abc'
```
### Test 8
**Input:**
```
''
''
```
**Output:**
```
''
```
### Test 9
**Input:**
```
'a'
'b'
```
**Output:**
```
'ab'
```
### Test 10
**Input:**
```
'ax'
'b'
```
**Output:**
```
'abx'
```
### Test 11
**Input:**
```
'a'
'bx'
```
**Output:**
```
'abx'
```
### Test 12
**Input:**
```
'So'
'Long'
```
**Output:**
```
'SLoong'
```
### Test 13
**Input:**
```
'Long'
'So'
```
**Output:**
```
'LSoong'
```

