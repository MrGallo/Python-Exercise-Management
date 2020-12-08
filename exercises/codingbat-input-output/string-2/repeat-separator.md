# repeat_separator



**Requirements:**
```eval_rst
- :ref:`fundamentals:if, else`
- :ref:`fundamentals:loop with a counter variable`
- :ref:`fundamentals:string building and filtering`

```


Get two strings from the user, the first will be a `word` and the second a separator (call it `sep`). Get a third input from the user, an integer called `count`. Output a new string made of `count` occurrences of the word, separated by the separator string.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p109637) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
'Word'
'X'
3
```
**Output:**
```
'WordXWordXWord'
```
### Test 2
**Input:**
```
'This'
'And'
2
```
**Output:**
```
'ThisAndThis'
```
### Test 3
**Input:**
```
'This'
'And'
1
```
**Output:**
```
'This'
```
### Test 4
**Input:**
```
'Hi'
'-n-'
2
```
**Output:**
```
'Hi-n-Hi'
```
### Test 5
**Input:**
```
'AAA'
''
1
```
**Output:**
```
'AAA'
```
### Test 6
**Input:**
```
'AAA'
''
0
```
**Output:**
```
''
```
### Test 7
**Input:**
```
'A'
'B'
5
```
**Output:**
```
'ABABABABA'
```
### Test 8
**Input:**
```
'abc'
'XX'
3
```
**Output:**
```
'abcXXabcXXabc'
```
### Test 9
**Input:**
```
'abc'
'XX'
2
```
**Output:**
```
'abcXXabc'
```
### Test 10
**Input:**
```
'abc'
'XX'
1
```
**Output:**
```
'abc'
```
### Test 11
**Input:**
```
'XYZ'
'a'
2
```
**Output:**
```
'XYZaXYZ'
```

