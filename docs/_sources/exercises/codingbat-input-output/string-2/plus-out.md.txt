# plus_out




Given a string and a non-empty <b>word</b> string, return a version of the original String where all chars have been replaced by pluses ("+"), except for appearances of the word string which are preserved unchanged.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p170829) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






## Tests
### Test 1
#### Input
```
'12xy34'
'xy'
```
#### Output
```
'++xy++'
```
### Test 2
#### Input
```
'12xy34'
'1'
```
#### Output
```
'1+++++'
```
### Test 3
#### Input
```
'12xy34xyabcxy'
'xy'
```
#### Output
```
'++xy++xy+++xy'
```
### Test 4
#### Input
```
'abXYabcXYZ'
'ab'
```
#### Output
```
'ab++ab++++'
```
### Test 5
#### Input
```
'abXYabcXYZ'
'abc'
```
#### Output
```
'++++abc+++'
```
### Test 6
#### Input
```
'abXYabcXYZ'
'XY'
```
#### Output
```
'++XY+++XY+'
```
### Test 7
#### Input
```
'abXYxyzXYZ'
'XYZ'
```
#### Output
```
'+++++++XYZ'
```
### Test 8
#### Input
```
'--++ab'
'++'
```
#### Output
```
'++++++'
```
### Test 9
#### Input
```
'aaxxxxbb'
'xx'
```
#### Output
```
'++xxxx++'
```
### Test 10
#### Input
```
'123123'
'3'
```
#### Output
```
'++3++3'
```

