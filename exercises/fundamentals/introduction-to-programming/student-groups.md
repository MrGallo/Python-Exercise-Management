# Student Groups
**Topic:** mathematical calculations



Modulus (remainder) is one of the stranger mathematical operators, but its use in computer science is incredibly important. We also use modulus on a daily basis but don't think too much about it.

Given a class size of `33` students and the number of groups being `5`, the starter code is trying to determine the number of `students_per_group` as well as how many students will not be placed in a group (`students_left_over`). Leave the `students` and `number_of_groups` variables alone. Only modify the lines that have `students_per_group = 0` and `students_left_over = 0`.

Use floor division to determine the number of students per group and modulus to determine the number of left over students. 

Here is a table of [Python Mathematical Operators](https://gist.github.com/MrGallo/f6ef9b3ef06875761a675730e1095af6).

## Starter Code
```python
students = 33
number_of_groups = 5

students_per_group = 0
students_left_over = 0

print(f"If there are {students} students and {number_of_groups} groups.")
print(f"There will be {students_per_group} students per group")
print(f"and there will be {students_left_over} students without a group.")
```

## Tests
```python
from exercise.fixtures import captured_output, source_code_matches


def test_correct_students_per_group(captured_output):
    assert "There will be 6 students per group" in captured_output()


def test_using_proper_math_to_calculate_students_per_group():
    assert len(source_code_matches(r"students_per_group\s?=\s?students\s?\/\/\s?number_of_groups")), "You must use mathematical operations to solve this. Also, you need to use the proper variables. Don't simply repeat the values stored in the variables."


def test_correct_students_remaining(captured_output):
    assert "and there will be 3 students without a group." in captured_output()


def test_using_proper_math_to_calculate_students_remaining():
    assert len(source_code_matches(r"students_left_over\s?=\s?students\s?%\s?number_of_groups")), "You must use mathematical operations to solve this. Also, you need to use the proper variables. Don't simply repeat the values stored in the variables."
```
