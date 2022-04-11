# zero_max





Return a version of the given list where each zero value in the list is replaced by the largest odd value to the right of the zero in the list. If there is no odd value to the right of the zero, leave the zero as a zero.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p187050) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
[0, 5, 0, 3]
```
**Output:**
```
[5, 5, 3, 3]
```
### Test 2
**Input:**
```
[0, 4, 0, 3]
```
**Output:**
```
[3, 4, 3, 3]
```
### Test 3
**Input:**
```
[0, 1, 0]
```
**Output:**
```
[1, 1, 0]
```
### Test 4
**Input:**
```
[0, 1, 5]
```
**Output:**
```
[5, 1, 5]
```
### Test 5
**Input:**
```
[0, 2, 0]
```
**Output:**
```
[0, 2, 0]
```
### Test 6
**Input:**
```
[1]
```
**Output:**
```
[1]
```
### Test 7
**Input:**
```
[0]
```
**Output:**
```
[0]
```
### Test 8
**Input:**
```
[]
```
**Output:**
```
[]
```
### Test 9
**Input:**
```
[7, 0, 4, 3, 0, 2]
```
**Output:**
```
[7, 3, 4, 3, 0, 2]
```
### Test 10
**Input:**
```
[7, 0, 4, 3, 0, 1]
```
**Output:**
```
[7, 3, 4, 3, 1, 1]
```
### Test 11
**Input:**
```
[7, 0, 4, 3, 0, 0]
```
**Output:**
```
[7, 3, 4, 3, 0, 0]
```
### Test 12
**Input:**
```
[7, 0, 1, 0, 0, 7]
```
**Output:**
```
[7, 7, 1, 7, 7, 7]
```

