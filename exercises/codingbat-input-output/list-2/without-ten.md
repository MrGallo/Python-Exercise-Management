# without_ten





Return a version of the given list where all the 10's have been removed. The remaining elements should shift left towards the start of the list as needed, and the empty spaces a the end of the list should be 0. So {1, 10, 10, 2} yields {1, 2, 0, 0}. You may modify and return the given list or make a new list.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p196976) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
[1, 10, 10, 2]
```
**Output:**
```
[1, 2, 0, 0]
```
### Test 2
**Input:**
```
[10, 2, 10]
```
**Output:**
```
[2, 0, 0]
```
### Test 3
**Input:**
```
[1, 99, 10]
```
**Output:**
```
[1, 99, 0]
```
### Test 4
**Input:**
```
[10, 13, 10, 14]
```
**Output:**
```
[13, 14, 0, 0]
```
### Test 5
**Input:**
```
[10, 13, 10, 14, 10]
```
**Output:**
```
[13, 14, 0, 0, 0]
```
### Test 6
**Input:**
```
[10, 10, 3]
```
**Output:**
```
[3, 0, 0]
```
### Test 7
**Input:**
```
[1]
```
**Output:**
```
[1]
```
### Test 8
**Input:**
```
[13, 1]
```
**Output:**
```
[13, 1]
```
### Test 9
**Input:**
```
[10]
```
**Output:**
```
[0]
```
### Test 10
**Input:**
```
[]
```
**Output:**
```
[]
```

