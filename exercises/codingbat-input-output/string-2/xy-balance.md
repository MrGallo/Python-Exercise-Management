# xy_balance




We'll say that a String is xy-balanced if for all the 'x' chars in the string, there exists a 'y' char somewhere later in the string. So "xxy" is balanced, but "xyx" is not. One 'y' can balance multiple 'x's. Return true if the given string is xy-balanced.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p134250) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






## Tests
### Test 1
#### Input
```
'aaxbby'
```
#### Output
```
True
```
### Test 2
#### Input
```
'aaxbb'
```
#### Output
```
False
```
### Test 3
#### Input
```
'yaaxbb'
```
#### Output
```
False
```
### Test 4
#### Input
```
'yaaxbby'
```
#### Output
```
True
```
### Test 5
#### Input
```
'xaxxbby'
```
#### Output
```
True
```
### Test 6
#### Input
```
'xaxxbbyx'
```
#### Output
```
False
```
### Test 7
#### Input
```
'xxbxy'
```
#### Output
```
True
```
### Test 8
#### Input
```
'xxbx'
```
#### Output
```
False
```
### Test 9
#### Input
```
'bbb'
```
#### Output
```
True
```
### Test 10
#### Input
```
'bxbb'
```
#### Output
```
False
```
### Test 11
#### Input
```
'bxyb'
```
#### Output
```
True
```
### Test 12
#### Input
```
'xy'
```
#### Output
```
True
```
### Test 13
#### Input
```
'y'
```
#### Output
```
True
```
### Test 14
#### Input
```
'x'
```
#### Output
```
False
```
### Test 15
#### Input
```
''
```
#### Output
```
True
```
### Test 16
#### Input
```
'yxyxyxyx'
```
#### Output
```
False
```
### Test 17
#### Input
```
'yxyxyxyxy'
```
#### Output
```
True
```
### Test 18
#### Input
```
'12xabxxydxyxyzz'
```
#### Output
```
True
```

