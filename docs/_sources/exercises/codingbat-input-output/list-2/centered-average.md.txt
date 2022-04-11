# centered_average





Return the "centered" average of a list of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the list. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the list is length 3 or more.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p136585) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
[1, 2, 3, 4, 100]
```
**Output:**
```
3
```
### Test 2
**Input:**
```
[1, 1, 5, 5, 10, 8, 7]
```
**Output:**
```
5
```
### Test 3
**Input:**
```
[-10, -4, -2, -4, -2, 0]
```
**Output:**
```
-3
```
### Test 4
**Input:**
```
[5, 3, 4, 6, 2]
```
**Output:**
```
4
```
### Test 5
**Input:**
```
[5, 3, 4, 0, 100]
```
**Output:**
```
4
```
### Test 6
**Input:**
```
[100, 0, 5, 3, 4]
```
**Output:**
```
4
```
### Test 7
**Input:**
```
[4, 0, 100]
```
**Output:**
```
4
```
### Test 8
**Input:**
```
[0, 2, 3, 4, 100]
```
**Output:**
```
3
```
### Test 9
**Input:**
```
[1, 1, 100]
```
**Output:**
```
1
```
### Test 10
**Input:**
```
[7, 7, 7]
```
**Output:**
```
7
```
### Test 11
**Input:**
```
[1, 7, 8]
```
**Output:**
```
7
```
### Test 12
**Input:**
```
[1, 1, 99, 99]
```
**Output:**
```
50
```
### Test 13
**Input:**
```
[1000, 0, 1, 99]
```
**Output:**
```
50
```
### Test 14
**Input:**
```
[4, 4, 4, 4, 5]
```
**Output:**
```
4
```
### Test 15
**Input:**
```
[4, 4, 4, 1, 5]
```
**Output:**
```
4
```
### Test 16
**Input:**
```
[6, 4, 8, 12, 3]
```
**Output:**
```
6
```

