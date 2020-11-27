# make_tags




The web is built with HTML strings like "&lt;i&gt;Yay&lt;/i&gt;" which draws Yay as italic text. In this example, the "i" tag makes &lt;i&gt; and &lt;/i&gt; which surround the word "Yay". Ask the user for a tag string, then ask the user for a word string. Print out the HTML string with tags around the word, e.g. "&lt;i&gt;Yay&lt;/i&gt;".

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p147483) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
'i'
'Yay'
```
**Output:**
```
'<i>Yay</i>'
```
### Test 2
**Input:**
```
'i'
'Hello'
```
**Output:**
```
'<i>Hello</i>'
```
### Test 3
**Input:**
```
'cite'
'Yay'
```
**Output:**
```
'<cite>Yay</cite>'
```
### Test 4
**Input:**
```
'address'
'here'
```
**Output:**
```
'<address>here</address>'
```
### Test 5
**Input:**
```
'body'
'Heart'
```
**Output:**
```
'<body>Heart</body>'
```
### Test 6
**Input:**
```
'i'
'i'
```
**Output:**
```
'<i>i</i>'
```
### Test 7
**Input:**
```
'i'
''
```
**Output:**
```
'<i></i>'
```

