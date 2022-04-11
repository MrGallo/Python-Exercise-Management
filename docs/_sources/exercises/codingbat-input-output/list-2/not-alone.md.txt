# not_alone





We'll say that an element in a list is "alone" if there are values before and after it, and those values are different from it. Return a version of the given list where every instance of the given value which is alone is replaced by whichever value to its left or right is larger.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p169506) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
[1, 2, 3]
2
```
**Output:**
```
[1, 3, 3]
```
### Test 2
**Input:**
```
[1, 2, 3, 2, 5, 2]
2
```
**Output:**
```
[1, 3, 3, 5, 5, 2]
```
### Test 3
**Input:**
```
[3, 4]
3
```
**Output:**
```
[3, 4]
```
### Test 4
**Input:**
```
[3, 3]
3
```
**Output:**
```
[3, 3]
```
### Test 5
**Input:**
```
[1, 3, 1, 2]
1
```
**Output:**
```
[1, 3, 3, 2]
```
### Test 6
**Input:**
```
[3]
3
```
**Output:**
```
[3]
```
### Test 7
**Input:**
```
[]
3
```
**Output:**
```
[]
```
### Test 8
**Input:**
```
[7, 1, 6]
1
```
**Output:**
```
[7, 7, 6]
```
### Test 9
**Input:**
```
[1, 1, 1]
1
```
**Output:**
```
[1, 1, 1]
```
### Test 10
**Input:**
```
[1, 1, 1, 2]
1
```
**Output:**
```
[1, 1, 1, 2]
```

