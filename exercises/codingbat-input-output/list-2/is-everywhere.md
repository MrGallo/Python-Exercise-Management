# is_everywhere





We'll say that a value is "everywhere" in a list if for every pair of adjacent elements in the list, at least one of the pair is that value. Return true if the given value is everywhere in the list.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p110222) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
[1, 2, 1, 3]
1
```
**Output:**
```
True
```
### Test 2
**Input:**
```
[1, 2, 1, 3]
2
```
**Output:**
```
False
```
### Test 3
**Input:**
```
[1, 2, 1, 3, 4]
1
```
**Output:**
```
False
```
### Test 4
**Input:**
```
[2, 1, 2, 1]
1
```
**Output:**
```
True
```
### Test 5
**Input:**
```
[2, 1, 2, 1]
2
```
**Output:**
```
True
```
### Test 6
**Input:**
```
[2, 1, 2, 3, 1]
2
```
**Output:**
```
False
```
### Test 7
**Input:**
```
[3, 1]
3
```
**Output:**
```
True
```
### Test 8
**Input:**
```
[3, 1]
2
```
**Output:**
```
False
```
### Test 9
**Input:**
```
[3]
1
```
**Output:**
```
True
```
### Test 10
**Input:**
```
[]
1
```
**Output:**
```
True
```
### Test 11
**Input:**
```
[1, 2, 1, 2, 3, 2, 5]
2
```
**Output:**
```
True
```
### Test 12
**Input:**
```
[1, 2, 1, 1, 1, 2]
2
```
**Output:**
```
False
```
### Test 13
**Input:**
```
[2, 1, 2, 1, 1, 2]
2
```
**Output:**
```
False
```
### Test 14
**Input:**
```
[2, 1, 2, 2, 2, 1, 1, 2]
2
```
**Output:**
```
False
```
### Test 15
**Input:**
```
[2, 1, 2, 2, 2, 1, 2, 1]
2
```
**Output:**
```
True
```
### Test 16
**Input:**
```
[2, 1, 2, 1, 2]
2
```
**Output:**
```
True
```

