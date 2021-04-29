# Above Average



**Requirements:**
```eval_rst
- :ref:`fundamentals:defining a function`
- :ref:`fundamentals:defining parameters`
- :ref:`fundamentals:loop through a list (for)`
- :ref:`fundamentals:loop with an accumulator variable`
- :ref:`fundamentals:list building and filtering`
- :ref:`fundamentals:returning a value`

```


From scratch, code the function given the description below:

```
students_above_average(student_final_marks: Dict) -> List
```

The function will determine what the average mark is, based on all the marks in the given dictionary. It will then return a list of all students whose marks are *above* that average. The dictionary has the structure of:

```
key: value
name (str): mark (int)
```

For example:
```python
{
    "Jeff": 60,
    "Sally": 70,
    "Bob": 80
}
```

Answer:

```
["Bob"]
```

In this instance, the average is `70`, so only Bob would make the list of above average students.






## Tests
```python
from itertools import count

from main import students_above_average


def test_students_above_average_example():
    students = {
        "Jeff": 60,
        "Sally": 70,
        "Bob": 80
    }

    assert students_above_average(students) == ["Bob"]


def test_students_above_average_empty():
    students = {"Jeff": 60}
    assert students_above_average(students) == []


def test_students_above_average():
    students = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
    }
    assert students_above_average(students) == ["e", "f", "g"]
```
