# ten_run





For each multiple of 10 in the given list, change all the values following it to be that multiple of 10, until encountering another multiple of 10. So {2, 10, 3, 4, 20, 5} yields {2, 10, 10, 10, 20, 20}.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p199484) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
[2, 10, 3, 4, 20, 5]
```
**Output:**
```
[2, 10, 10, 10, 20, 20]
```
### Test 2
**Input:**
```
[10, 1, 20, 2]
```
**Output:**
```
[10, 10, 20, 20]
```
### Test 3
**Input:**
```
[10, 1, 9, 20]
```
**Output:**
```
[10, 10, 10, 20]
```
### Test 4
**Input:**
```
[1, 2, 50, 1]
```
**Output:**
```
[1, 2, 50, 50]
```
### Test 5
**Input:**
```
[1, 20, 50, 1]
```
**Output:**
```
[1, 20, 50, 50]
```
### Test 6
**Input:**
```
[10, 10]
```
**Output:**
```
[10, 10]
```
### Test 7
**Input:**
```
[10, 2]
```
**Output:**
```
[10, 10]
```
### Test 8
**Input:**
```
[0, 2]
```
**Output:**
```
[0, 0]
```
### Test 9
**Input:**
```
[1, 2]
```
**Output:**
```
[1, 2]
```
### Test 10
**Input:**
```
[1]
```
**Output:**
```
[1]
```
### Test 11
**Input:**
```
[]
```
**Output:**
```
[]
```

