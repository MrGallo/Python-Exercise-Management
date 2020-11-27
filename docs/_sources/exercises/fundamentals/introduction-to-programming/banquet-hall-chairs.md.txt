# Banquet Hall Chairs

**Topic:** 
```eval_rst
:ref:`fundamentals:storing data in variables`

```



The program will calculate the total number of chairs in a banquet hall. This is determined by the number of tables and the number of chairs per table.

Initialize a variable called `tables` and assign it a value of `32`.

Then initialize a variable called `chairs_per_table`, and assign it a value of `9`.

The program will calculate the total chairs and then output a message.

## Starter Code
```python
# initialize tables here
# initialize chairs_per_table here

# do not modify the code below this line
total_chairs = tables * chairs_per_table
print(f"There are {total_chairs} chairs.")
```

## Tests
```python
from exercise.fixtures import captured_output, source_code_matches


def test_bottom_code_isnt_modified():
    assert len(source_code_matches(r'total_chairs = tables \* chairs_per_table\nprint\(f"There are {total_chairs} chairs."\)')) == 1, "You shouldn't modify the code at the bottom."

def test_calculates_correct_numner(captured_output):
    assert captured_output() == "There are 288 chairs."
```
