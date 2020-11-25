# same_star_char




Returns true if for every '*' (star) in the string, if there are chars both immediately before and after the star, they are the same.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p194491) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






## Tests
### Test 1
#### Input
```
'xy*yzz'
```
#### Output
```
True
```
### Test 2
#### Input
```
'xy*zzz'
```
#### Output
```
False
```
### Test 3
#### Input
```
'*xa*az'
```
#### Output
```
True
```
### Test 4
#### Input
```
'*xa*bz'
```
#### Output
```
False
```
### Test 5
#### Input
```
'*xa*a*'
```
#### Output
```
True
```
### Test 6
#### Input
```
''
```
#### Output
```
True
```
### Test 7
#### Input
```
'*xa*a*a'
```
#### Output
```
True
```
### Test 8
#### Input
```
'*xa*a*b'
```
#### Output
```
False
```
### Test 9
#### Input
```
'*12*2*2'
```
#### Output
```
True
```
### Test 10
#### Input
```
'12*2*3*'
```
#### Output
```
False
```
### Test 11
#### Input
```
'abcDEF'
```
#### Output
```
True
```
### Test 12
#### Input
```
'XY*YYYY*Z*'
```
#### Output
```
False
```
### Test 13
#### Input
```
'XY*YYYY*Y*'
```
#### Output
```
True
```
### Test 14
#### Input
```
'12*2*3*'
```
#### Output
```
False
```
### Test 15
#### Input
```
'*'
```
#### Output
```
True
```
### Test 16
#### Input
```
'**'
```
#### Output
```
True
```

