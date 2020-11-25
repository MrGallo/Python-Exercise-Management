# one_two




Given a string, compute a new string by moving the first char to come after the next two chars, so "abc" yields "bca". Repeat this process for each subsequent group of 3 chars, so "abcdef" yields "bcaefd". Ignore any group of fewer than 3 chars at the end.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p122943) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






## Tests
### Test 1
#### Input
```
'abc'
```
#### Output
```
'bca'
```
### Test 2
#### Input
```
'tca'
```
#### Output
```
'cat'
```
### Test 3
#### Input
```
'tcagdo'
```
#### Output
```
'catdog'
```
### Test 4
#### Input
```
'chocolate'
```
#### Output
```
'hocolctea'
```
### Test 5
#### Input
```
'1234567890'
```
#### Output
```
'231564897'
```
### Test 6
#### Input
```
'xabxabxabxabxabxabxab'
```
#### Output
```
'abxabxabxabxabxabxabx'
```
### Test 7
#### Input
```
'abcdefx'
```
#### Output
```
'bcaefd'
```
### Test 8
#### Input
```
'abcdefxy'
```
#### Output
```
'bcaefd'
```
### Test 9
#### Input
```
'abcdefxyz'
```
#### Output
```
'bcaefdyzx'
```
### Test 10
#### Input
```
''
```
#### Output
```
''
```
### Test 11
#### Input
```
'x'
```
#### Output
```
''
```
### Test 12
#### Input
```
'xy'
```
#### Output
```
''
```
### Test 13
#### Input
```
'xyz'
```
#### Output
```
'yzx'
```
### Test 14
#### Input
```
'abcdefghijklkmnopqrstuvwxyz1234567890'
```
#### Output
```
'bcaefdhigkljmnkpqostrvwuyzx231564897'
```
### Test 15
#### Input
```
'abcdefghijklkmnopqrstuvwxyz123456789'
```
#### Output
```
'bcaefdhigkljmnkpqostrvwuyzx231564897'
```
### Test 16
#### Input
```
'abcdefghijklkmnopqrstuvwxyz12345678'
```
#### Output
```
'bcaefdhigkljmnkpqostrvwuyzx231564'
```

