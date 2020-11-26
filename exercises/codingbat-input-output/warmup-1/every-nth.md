# every_nth




Given a non-empty string and an int N, return the string made starting with char 0, and then every Nth char of the string. So if N is 3, use char 0, 3, 6, ... and so on. N is 1 or more.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p196441) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






## Tests
### Test 1
**Input:**
```
'Miracle'
2
```
**Output:**
```
'Mrce'
```
### Test 2
**Input:**
```
'abcdefg'
2
```
**Output:**
```
'aceg'
```
### Test 3
**Input:**
```
'abcdefg'
3
```
**Output:**
```
'adg'
```
### Test 4
**Input:**
```
'Chocolate'
3
```
**Output:**
```
'Cca'
```
### Test 5
**Input:**
```
'Chocolates'
3
```
**Output:**
```
'Ccas'
```
### Test 6
**Input:**
```
'Chocolates'
4
```
**Output:**
```
'Coe'
```
### Test 7
**Input:**
```
'Chocolates'
100
```
**Output:**
```
'C'
```

