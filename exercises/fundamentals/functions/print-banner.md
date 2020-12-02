# Print Banner

**Topic:** 
```eval_rst
:ref:`fundamentals:defining a function`

```

**Requirements:**
```eval_rst
- :ref:`fundamentals:calling a function`

```


The starter text will print out a some ASCII art. Select all the lines and press tab to indent them all once. Right on top of the indented print statements, define a function called `print_banner`. The definition line should be `def print_banner():`

To ensure you did it correctly, call the function and run it.

Check out the [ASCII art generator](http://patorjk.com/software/taag).

## Starter Code
```python
print("  _    _      _ _         __          __        _     _ _ ")
print(" | |  | |    | | |        \ \        / /       | |   | | |")
print(" | |__| | ___| | | ___     \ \  /\  / /__  _ __| | __| | |")
print(" |  __  |/ _ \ | |/ _ \     \ \/  \/ / _ \| '__| |/ _` | |")
print(" | |  | |  __/ | | (_) |     \  /\  / (_) | |  | | (_| |_|")
print(" |_|  |_|\___|_|_|\___( )     \/  \/ \___/|_|  |_|\__,_(_)")
print("                      |/                                  ")
```

## Tests
```python
from exercise.fixtures import captured_output, source_code_matches

from main import print_banner


def test_function_defined_properly():
    assert len(source_code_matches(r'def\s+print_banner\s*\(\s*\)\s*:\s*')) == 1


def test_print_banner(capsys):
    print_banner()
    captured = capsys.readouterr()
    assert captured.out == """  _    _      _ _         __          __        _     _ _ 
 | |  | |    | | |        \ \        / /       | |   | | |
 | |__| | ___| | | ___     \ \  /\  / /__  _ __| | __| | |
 |  __  |/ _ \ | |/ _ \     \ \/  \/ / _ \| '__| |/ _` | |
 | |  | |  __/ | | (_) |     \  /\  / (_) | |  | | (_| |_|
 |_|  |_|\___|_|_|\___( )     \/  \/ \___/|_|  |_|\__,_(_)
                      |/                                  
"""
```
