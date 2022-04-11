# same_ends





Return true if the group of N numbers at the start and end of the list are the same. For example, with {5, 6, 45, 99, 13, 5, 6}, the ends are the same for n=0 and n=2, and false for n=1 and n=3. You may assume that n is in the range 0..nums.length inclusive.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p134300) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
[5, 6, 45, 99, 13, 5, 6]
1
```
**Output:**
```
False
```
### Test 2
**Input:**
```
[5, 6, 45, 99, 13, 5, 6]
2
```
**Output:**
```
True
```
### Test 3
**Input:**
```
[5, 6, 45, 99, 13, 5, 6]
3
```
**Output:**
```
False
```
### Test 4
**Input:**
```
[1, 2, 5, 2, 1]
1
```
**Output:**
```
True
```
### Test 5
**Input:**
```
[1, 2, 5, 2, 1]
2
```
**Output:**
```
False
```
### Test 6
**Input:**
```
[1, 2, 5, 2, 1]
0
```
**Output:**
```
True
```
### Test 7
**Input:**
```
[1, 2, 5, 2, 1]
5
```
**Output:**
```
True
```
### Test 8
**Input:**
```
[1, 1, 1]
0
```
**Output:**
```
True
```
### Test 9
**Input:**
```
[1, 1, 1]
1
```
**Output:**
```
True
```
### Test 10
**Input:**
```
[1, 1, 1]
2
```
**Output:**
```
True
```
### Test 11
**Input:**
```
[1, 1, 1]
3
```
**Output:**
```
True
```
### Test 12
**Input:**
```
[1]
1
```
**Output:**
```
True
```
### Test 13
**Input:**
```
[]
0
```
**Output:**
```
True
```
### Test 14
**Input:**
```
[4, 2, 4, 5]
1
```
**Output:**
```
False
```

