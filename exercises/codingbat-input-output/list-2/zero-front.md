# zero_front





Return a list that contains the exact same numbers as the given list, but rearranged so that all the zeros are grouped at the start of the list. The order of the non-zero numbers does not matter. So {1, 0, 0, 1} becomes {0 ,0, 1, 1}. You may modify and return the given list or make a new list.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p193753) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
[1, 0, 0, 1]
```
**Output:**
```
[0, 0, 1, 1]
```
### Test 2
**Input:**
```
[0, 1, 1, 0, 1]
```
**Output:**
```
[0, 0, 1, 1, 1]
```
### Test 3
**Input:**
```
[1, 0]
```
**Output:**
```
[0, 1]
```
### Test 4
**Input:**
```
[0, 1]
```
**Output:**
```
[0, 1]
```
### Test 5
**Input:**
```
[1, 1, 1, 0]
```
**Output:**
```
[0, 1, 1, 1]
```
### Test 6
**Input:**
```
[2, 2, 2, 2]
```
**Output:**
```
[2, 2, 2, 2]
```
### Test 7
**Input:**
```
[0, 0, 1, 0]
```
**Output:**
```
[0, 0, 0, 1]
```
### Test 8
**Input:**
```
[-1, 0, 0, -1, 0]
```
**Output:**
```
[0, 0, 0, -1, -1]
```
### Test 9
**Input:**
```
[0, -3, 0, -3]
```
**Output:**
```
[0, 0, -3, -3]
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
### Test 11
**Input:**
```
[9, 9, 0, 9, 0, 9]
```
**Output:**
```
[0, 0, 9, 9, 9, 9]
```

