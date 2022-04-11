# fizz_buzz





This is slightly more difficult version of the famous FizzBuzz problem which is sometimes given as a first problem for job interviews. (See also: <a href=/doc/practice/fizzbuzz-code.html>FizzBuzz Code</a>.) Consider the series of numbers beginning at <b>start</b> and running up to but not including <b>end</b>, so for example start=1 and end=5 gives the series 1, 2, 3, 4. Return a new String[] list containing the string form of these numbers, except for multiples of 3, use "Fizz" instead of the number, for multiples of 5 use "Buzz", and for multiples of both 3 and 5 use "FizzBuzz". In Java, String.valueOf(xxx) will make the String form of an int or other type. This version is a little more complicated than the usual version since you have to allocate and index into a list instead of just printing, and we vary the start/end instead of just always doing 1..100.

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p153059) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.






### Test 1
**Input:**
```
1
6
```
**Output:**
```
['1', '2', 'Fizz', '4', 'Buzz']
```
### Test 2
**Input:**
```
1
8
```
**Output:**
```
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7']
```
### Test 3
**Input:**
```
1
11
```
**Output:**
```
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']
```
### Test 4
**Input:**
```
1
16
```
**Output:**
```
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
```
### Test 5
**Input:**
```
1
4
```
**Output:**
```
['1', '2', 'Fizz']
```
### Test 6
**Input:**
```
1
2
```
**Output:**
```
['1']
```
### Test 7
**Input:**
```
50
56
```
**Output:**
```
['Buzz', 'Fizz', '52', '53', 'Fizz', 'Buzz']
```
### Test 8
**Input:**
```
15
17
```
**Output:**
```
['FizzBuzz', '16']
```
### Test 9
**Input:**
```
30
36
```
**Output:**
```
['FizzBuzz', '31', '32', 'Fizz', '34', 'Buzz']
```
### Test 10
**Input:**
```
1000
1006
```
**Output:**
```
['Buzz', '1001', 'Fizz', '1003', '1004', 'FizzBuzz']
```
### Test 11
**Input:**
```
99
102
```
**Output:**
```
['Fizz', 'Buzz', '101']
```
### Test 12
**Input:**
```
14
20
```
**Output:**
```
['14', 'FizzBuzz', '16', '17', 'Fizz', '19']
```

