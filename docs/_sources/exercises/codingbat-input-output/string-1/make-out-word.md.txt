# make_out_word




Given an "out" string length 4, such as "&lt;&lt;&gt;&gt;", and a word, return a new string where the word is in the middle of the out string, e.g. "&lt;&lt;word&gt;&gt;". Note: use str.substring(i, j) to extract the String starting at index i and going up to but not including index j.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p184030) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






## Tests
### Test 1
#### Input
```
'<<>>'
'Yay'
```
#### Output
```
'<<Yay>>'
```
### Test 2
#### Input
```
'<<>>'
'WooHoo'
```
#### Output
```
'<<WooHoo>>'
```
### Test 3
#### Input
```
'[[]]'
'word'
```
#### Output
```
'[[word]]'
```
### Test 4
#### Input
```
'HHoo'
'Hello'
```
#### Output
```
'HHHellooo'
```
### Test 5
#### Input
```
'abyz'
'YAY'
```
#### Output
```
'abYAYyz'
```

