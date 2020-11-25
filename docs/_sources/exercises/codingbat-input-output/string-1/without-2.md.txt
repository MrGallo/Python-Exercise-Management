# without_2




Given a string, if a length 2 substring appears at both its beginning and end, return a string without the substring at the beginning, so "HelloHe" yields "lloHe". The substring may overlap with itself, so "Hi" yields "". Otherwise, return the original string unchanged.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p142247) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






## Tests
### Test 1
#### Input
```
'HelloHe'
```
#### Output
```
'lloHe'
```
### Test 2
#### Input
```
'HelloHi'
```
#### Output
```
'HelloHi'
```
### Test 3
#### Input
```
'Hi'
```
#### Output
```
''
```
### Test 4
#### Input
```
'Chocolate'
```
#### Output
```
'Chocolate'
```
### Test 5
#### Input
```
'xxx'
```
#### Output
```
'x'
```
### Test 6
#### Input
```
'xx'
```
#### Output
```
''
```
### Test 7
#### Input
```
'x'
```
#### Output
```
'x'
```
### Test 8
#### Input
```
''
```
#### Output
```
''
```
### Test 9
#### Input
```
'Fruits'
```
#### Output
```
'Fruits'
```

