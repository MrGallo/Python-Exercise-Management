:orphan:


How to Practice
---------------

Exercise Runner
---------------
You can do these exercises and test them using my `Python Exercise Runner <https://repl.it/@DanielGallo/Python-Exercise-Runner>`_.


Copy and paste to your computer
-------------------------

- Copy and paste the starter code into a file called ``main.py``.

You can either test it manually by running the file and providing the program its own inputs and visually verifying the output.

Or you can run ``pytest`` to check it for you:

- Copy and paste the test code into a file called ``test_main.py``.
- Complete the exercise in ``main.py``.
- In the terminal run ``pytest`` (needs to be installed)

.. warning:: Under construction


# Exercise Runner

This replit will fetch and run automated tests for a selection of exercises which can be found at my [Python Exercises](https://mrgallo.github.io/python-exercises) website.

- [Exercise Runner](#exercise-runner)
  * [Quick reference](#quick-reference)
  * [Get a new Exercise](#get-a-new-exercise)
  * [Testing your Solution](#testing-your-solution)
    + [Manually](#manually)
    + [Automated tests](#automated-tests)
  * [Submitting your solution](#submitting-your-solution)


## Quick Reference
Go into the replit.com **Shell** tab to execute the following commands.
```sh
$ python -m exercise.get
$ python -m exercise.test
$ python -m exercise.submit
```

## Get a new Exercise

1. Open the Shell (Linux Terminal).
    - In the Replit.com window go into the "Shell" tab.
2. Run `python -m exercise.get` in the terminal.
3. Select an exercise to attempt.
4. Any starter code will be written into the `main.py` file.
    - *Warning*: This will overwrite anything you may have had in there.
5. The instructions for the exercise will be found in `instructions.md`.
    - Be sure to go into the "Markdown" tab to view it with proper formatting.

## Testing your Solution
### Manually
Hit "Run" at the top and manually test your program.

If you are writing functions, you will need to actualy call the function
with valid arguments and then print out the result so you can see it.

Take for example the following function:

```python
def greet(name: str) -> str:
    return f"Greetings, {name}."
```

In order to run this manually, you need to call the function and print out the result.
Somewhere below (and outside of) the function, 
```python
result = greet("Dave")
print(result)
```
All together:
```python
def greet(name: str) -> str:
    return f"Greetings, {name}."


result = greet("Dave")
print(result)
```

Outputs:
```
Greetings, Dave.
```
### Automated tests
1. Open the Shell (Linux Terminal).
    - In the Replit.com window go into the "Shell" tab.
2. Run `python -m exercise.test` in the terminal.
3. Outcomes:
    - **Failed**: if the tests fail, you will see *red text* and the output will let you know:
        - On what *line number* the error happend
        - What the difference was between your result and the expected result.
    - **Passed**: if the tests pass, you will see *green text*.
        - You can then move on to submit your solution

## Submitting your solution

1. Open the Shell (Linux Terminal).
    - In the Replit.com window go into the "Shell" tab.
2. Run `python -m exercise.submit` in the terminal.
    - This will run the tests and submit the solution.
    - If the tests do not pass, you will be given the option to submit anyway.
