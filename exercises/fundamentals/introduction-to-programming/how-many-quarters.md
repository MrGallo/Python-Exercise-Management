# How Many Quarters?
**Topic:** mathematical operations



Floor division is useful when we need to know how many times we can evenly divide a particular number.

Imagine you are at the store and you pay cash for something and the amount of money they need to give back to you is `$2.35`. Also imagine, for the sake of the exercise, the highest valued coins they have are quarters to give back to you. 

The starter code tries to determine how many quarters they will need to give back to you. Modify the line with `quarters = 0` to determine the number of quarters required.

*Note: the code will handle currency in cents rather than dollars.*

## Starter Code
```python
change_cents = 235
quarters = 0

print(f"You will get back {quarters} quarters.")
```

## Tests
```python
from exercise.fixtures import captured_output, source_code_matches


def test_calculates_correct_quarters(captured_output):
    assert "You will get back 9 quarters." in captured_output()


def test_proper_calculation_for_quarters():
    assert len(source_code_matches(r"quarters\s?=\s?change_cents\s?\/\/\s?25")) == 1, "There should be a mathematical operation in your source code. Also, use the 'change_cents' variable to calculate this."
```
