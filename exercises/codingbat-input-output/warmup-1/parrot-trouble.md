# parrot_trouble




We have a loud talking parrot. Get an hour from the user. The "hour" is the current hour time in the range `0..23`. We are in trouble if the parrot is talking and the hour is before `7` or after `20`. Output if we are in trouble or not. For the test cases below, `False` means "no" and `True` means "yes".

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p140449) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
True
6
```
**Output:**
```
True
```
### Test 2
**Input:**
```
True
7
```
**Output:**
```
False
```
### Test 3
**Input:**
```
False
6
```
**Output:**
```
False
```
### Test 4
**Input:**
```
True
21
```
**Output:**
```
True
```
### Test 5
**Input:**
```
False
21
```
**Output:**
```
False
```
### Test 6
**Input:**
```
False
20
```
**Output:**
```
False
```
### Test 7
**Input:**
```
True
23
```
**Output:**
```
True
```
### Test 8
**Input:**
```
False
23
```
**Output:**
```
False
```
### Test 9
**Input:**
```
True
20
```
**Output:**
```
False
```
### Test 10
**Input:**
```
False
12
```
**Output:**
```
False
```

