# missing_char




Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..str.length()-1 inclusive).

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p190570) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
'kitten'
1
```
**Output:**
```
'ktten'
```
### Test 2
**Input:**
```
'kitten'
0
```
**Output:**
```
'itten'
```
### Test 3
**Input:**
```
'kitten'
4
```
**Output:**
```
'kittn'
```
### Test 4
**Input:**
```
'Hi'
0
```
**Output:**
```
'i'
```
### Test 5
**Input:**
```
'Hi'
1
```
**Output:**
```
'H'
```
### Test 6
**Input:**
```
'code'
0
```
**Output:**
```
'ode'
```
### Test 7
**Input:**
```
'code'
1
```
**Output:**
```
'cde'
```
### Test 8
**Input:**
```
'code'
2
```
**Output:**
```
'coe'
```
### Test 9
**Input:**
```
'code'
3
```
**Output:**
```
'cod'
```
### Test 10
**Input:**
```
'chocolate'
8
```
**Output:**
```
'chocolat'
```

