# repeat_front





Given a string and an int n, return a string made of the first n characters of the string, followed by the first n-1 characters of the string, and so on. You may assume that n is between 0 and the length of the string, inclusive (i.e. n &gt;= 0 and n &lt;= str.length()).

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p128796) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
'Chocolate'
4
```
**Output:**
```
'ChocChoChC'
```
### Test 2
**Input:**
```
'Chocolate'
3
```
**Output:**
```
'ChoChC'
```
### Test 3
**Input:**
```
'Ice Cream'
2
```
**Output:**
```
'IcI'
```
### Test 4
**Input:**
```
'Ice Cream'
1
```
**Output:**
```
'I'
```
### Test 5
**Input:**
```
'Ice Cream'
0
```
**Output:**
```
''
```
### Test 6
**Input:**
```
'xyz'
3
```
**Output:**
```
'xyzxyx'
```
### Test 7
**Input:**
```
''
0
```
**Output:**
```
''
```
### Test 8
**Input:**
```
'Java'
4
```
**Output:**
```
'JavaJavJaJ'
```
### Test 9
**Input:**
```
'Java'
1
```
**Output:**
```
'J'
```

