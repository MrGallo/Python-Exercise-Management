# make_2





Given 2 int lists, a and b, return a new list length 2 containing, as much as will fit, the elements from a followed by the elements from b. The lists may be any length, including 0, but there will be 2 or more elements available between the 2 lists.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p143461) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
[4, 5]
[1, 2, 3]
```
**Output:**
```
[4, 5]
```
### Test 2
**Input:**
```
[4]
[1, 2, 3]
```
**Output:**
```
[4, 1]
```
### Test 3
**Input:**
```
[]
[1, 2]
```
**Output:**
```
[1, 2]
```
### Test 4
**Input:**
```
[1, 2]
[]
```
**Output:**
```
[1, 2]
```
### Test 5
**Input:**
```
[3]
[1, 2, 3]
```
**Output:**
```
[3, 1]
```
### Test 6
**Input:**
```
[3]
[1]
```
**Output:**
```
[3, 1]
```
### Test 7
**Input:**
```
[3, 1, 4]
[]
```
**Output:**
```
[3, 1]
```
### Test 8
**Input:**
```
[1]
[1]
```
**Output:**
```
[1, 1]
```
### Test 9
**Input:**
```
[1, 2, 3]
[7, 8]
```
**Output:**
```
[1, 2]
```
### Test 10
**Input:**
```
[7, 8]
[1, 2, 3]
```
**Output:**
```
[7, 8]
```
### Test 11
**Input:**
```
[7]
[1, 2, 3]
```
**Output:**
```
[7, 1]
```
### Test 12
**Input:**
```
[5, 4]
[2, 3, 7]
```
**Output:**
```
[5, 4]
```

