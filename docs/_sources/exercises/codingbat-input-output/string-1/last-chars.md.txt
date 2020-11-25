# last_chars




Given 2 strings, a and b, return a new string made of the first char of a and the last char of b, so "yo" and "java" yields "ya". If either string is length 0, use '@' for its missing char.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p138183) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






## Tests
### Test 1
#### Input
```
'last'
'chars'
```
#### Output
```
'ls'
```
### Test 2
#### Input
```
'yo'
'java'
```
#### Output
```
'ya'
```
### Test 3
#### Input
```
'hi'
''
```
#### Output
```
'h@'
```
### Test 4
#### Input
```
''
'hello'
```
#### Output
```
'@o'
```
### Test 5
#### Input
```
''
''
```
#### Output
```
'@@'
```
### Test 6
#### Input
```
'kitten'
'hi'
```
#### Output
```
'ki'
```
### Test 7
#### Input
```
'k'
'zip'
```
#### Output
```
'kp'
```
### Test 8
#### Input
```
'kitten'
''
```
#### Output
```
'k@'
```
### Test 9
#### Input
```
'kitten'
'zip'
```
#### Output
```
'kp'
```

