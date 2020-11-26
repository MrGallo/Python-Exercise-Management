# zip_zap




Look for patterns like "zip" and "zap" in the string -- length-3, starting with 'z' and ending with 'p'. Return a string where for all such words, the middle letter is gone, so "zipXzap" yields "zpXzp".

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p180759) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






## Tests
### Test 1
**Input:**
```
'zipXzap'
```
**Output:**
```
'zpXzp'
```
### Test 2
**Input:**
```
'zopzop'
```
**Output:**
```
'zpzp'
```
### Test 3
**Input:**
```
'zzzopzop'
```
**Output:**
```
'zzzpzp'
```
### Test 4
**Input:**
```
'zibzap'
```
**Output:**
```
'zibzp'
```
### Test 5
**Input:**
```
'zip'
```
**Output:**
```
'zp'
```
### Test 6
**Input:**
```
'zi'
```
**Output:**
```
'zi'
```
### Test 7
**Input:**
```
'z'
```
**Output:**
```
'z'
```
### Test 8
**Input:**
```
''
```
**Output:**
```
''
```
### Test 9
**Input:**
```
'zzp'
```
**Output:**
```
'zp'
```
### Test 10
**Input:**
```
'abcppp'
```
**Output:**
```
'abcppp'
```
### Test 11
**Input:**
```
'azbcppp'
```
**Output:**
```
'azbcppp'
```
### Test 12
**Input:**
```
'azbcpzpp'
```
**Output:**
```
'azbcpzp'
```

