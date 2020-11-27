# All the Operators

**Topic:** ```eval_rst
:ref:`fundamentals:mathematical calculations`

```



Python can do mathematical evaluations, but some of the symbols are different than you might be used to.

Check out the [Python Mathematical Operators](https://gist.github.com/MrGallo/f6ef9b3ef06875761a675730e1095af6) table.

The starter code is missing the mathematical equations. In the empty `print()` functions, place the appropriate math. The first one is done for you.

## Starter Code
```python
print("One plus Two is:")
print(1 + 2)

print("Five minus Three is:")
print()

print("Six multiplied by Four is:")
print()

print("Twelve divided by Six is:")
print()

print("Twenty Three floor-divide by Five is:")
print()

print("The remainder of Twenty Three divided by Five is:")
print()

print("Two to the power of Eight is:")
print()
```

## Tests
```python
from exercise.fixtures import captured_output, source_code_matches


def test_one_plus_two(captured_output):
    assert "One plus Two is:\n3" in captured_output()


def test_contains_mathematical_expression_1_plus_2():
    assert source_code_matches(r"print\(\s?1\s?\+\s?2\s?\)") or source_code_matches(r"print\(\s?2\s?\+\s?1\s?\)"), "There should be a mathematical expression in your code (1 + 2)."


def test_five_minus_three(captured_output):
    assert "Five minus Three is:\n2" in captured_output()


def test_contains_mathematical_expression_5_minus_3():
    assert source_code_matches(r"print\(\s?5\s?\-\s?3\s?\)"), "There should be a mathematical expression in your code (5 - 3)."


def test_six_multiply_four(captured_output):
    assert "Six multiplied by Four is:\n24" in captured_output()


def test_contains_mathematical_expression_6_multiply_4():
    assert source_code_matches(r"print\(\s?6\s?\*\s?4s?\)") or source_code_matches(r"print\(\s?4\s?\*\s?6s?\)"), "There should be a mathematical expression in your code (6 * 4)."


def test_twelve_divide_by_6(captured_output):
    assert "Twelve divided by Six is:\n2" in captured_output()


def test_contains_mathematical_expression_12_divide_6():
    assert source_code_matches(r"print\(\s?12\s?/\s?6\s?\)"), "There should be a mathematical expression in your code (12 / 6)."


def test_23_floor_divide_5(captured_output):
    assert "Twenty Three floor-divide by Five is:\n4" in captured_output()


def test_contains_mathematical_expression_23_floor_5():
    assert source_code_matches(r"print\(\s?23\s?//\s?5\s?\)"), "There should be a mathematical expression in your code (23 // 5)."


def test_2_power_8(captured_output):
    assert "Two to the power of Eight is:\n256" in captured_output()


def test_contains_mathematical_expression_2_power_8():
    assert source_code_matches(r"print\(\s?2\s?\*\*\s?8\s?\)"), "There should be a mathematical expression in your code (2 ** 8)."
```
