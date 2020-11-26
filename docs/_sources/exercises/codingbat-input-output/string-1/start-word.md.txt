# start_word




Given a string and a second "word" string, we'll say that the word matches the string if it appears at the front of the string, except its first char does not need to match exactly. On a match, return the front of the string, or otherwise return the empty string. So, so with the string "hippo" the word "hi" returns "hi" and "xip" returns "hip". The word will be at least length 1.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p141494) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
'hippo'
'hi'
```
**Output:**
```
'hi'
```
### Test 2
**Input:**
```
'hippo'
'xip'
```
**Output:**
```
'hip'
```
### Test 3
**Input:**
```
'hippo'
'i'
```
**Output:**
```
'h'
```
### Test 4
**Input:**
```
'hippo'
'ix'
```
**Output:**
```
''
```
### Test 5
**Input:**
```
'h'
'ix'
```
**Output:**
```
''
```
### Test 6
**Input:**
```
''
'i'
```
**Output:**
```
''
```
### Test 7
**Input:**
```
'hip'
'zi'
```
**Output:**
```
'hi'
```
### Test 8
**Input:**
```
'hip'
'zip'
```
**Output:**
```
'hip'
```
### Test 9
**Input:**
```
'hip'
'zig'
```
**Output:**
```
''
```
### Test 10
**Input:**
```
'h'
'z'
```
**Output:**
```
'h'
```
### Test 11
**Input:**
```
'hippo'
'xippo'
```
**Output:**
```
'hippo'
```
### Test 12
**Input:**
```
'hippo'
'xyz'
```
**Output:**
```
''
```
### Test 13
**Input:**
```
'hippo'
'hip'
```
**Output:**
```
'hip'
```
### Test 14
**Input:**
```
'kitten'
'cit'
```
**Output:**
```
'kit'
```
### Test 15
**Input:**
```
'kit'
'cit'
```
**Output:**
```
'kit'
```

