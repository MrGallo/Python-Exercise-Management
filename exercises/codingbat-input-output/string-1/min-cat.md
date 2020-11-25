# min_cat




Given two strings, append them together (known as "concatenation") and return the result. However, if the strings are different lengths, omit chars from the longer string so it is the same length as the shorter string. So "Hello" and "Hi" yield "loHi". The strings may be any length.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p105745) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






## Tests
### Test 1
#### Input
```
'Hello'
'Hi'
```
#### Output
```
'loHi'
```
### Test 2
#### Input
```
'Hello'
'java'
```
#### Output
```
'ellojava'
```
### Test 3
#### Input
```
'java'
'Hello'
```
#### Output
```
'javaello'
```
### Test 4
#### Input
```
'abc'
'x'
```
#### Output
```
'cx'
```
### Test 5
#### Input
```
'x'
'abc'
```
#### Output
```
'xc'
```
### Test 6
#### Input
```
'abc'
''
```
#### Output
```
''
```

