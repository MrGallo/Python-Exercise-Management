# Do my homework

**Topic:** 
```eval_rst
:ref:`fundamentals:passing arguments`

```

**Requirements:**
```eval_rst
- :ref:`fundamentals:calling a function`

```


Sometimes we can think of functions as our friends waiting to do some job for us. This function is a friend who is willing to complete your homework for you. You can't just say "Hey friend, finish my homework" because they would have no idea what class or chapter you want them to complete.

Pass the `get_friend_to_do_your_homework` function two arguments. The first should be a string of the name of the subject, the second argument should be a string, the name of the chapter you need them to complete.

Once you give your 'friend' that information, they can go and complete your homework for them. Try sending them `"math"` for the subject and `"functions"` for the chapter. The result output should be:

```
Ok, I'll complete the functions chapter of your math work.
```

## Starter Code
```python
def get_friend_to_do_your_homework(subject: str, chapter: str) -> None:
    print(f"Ok, I'll complete the {chapter} chapter of your {subject} work.")


get_friend_to_do_your_homework()
```

## Tests
```python
from exercise.fixtures import captured_output


def test_do_homework(captured_output):
    assert captured_output() == "Ok, I'll complete the functions chapter of your math work."
```
