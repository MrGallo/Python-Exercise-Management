# Exercise Runner

[![Run on Repl.it](https://repl.it/badge/github/MrGallo/Python-Exercises)](https://repl.it/github/MrGallo/Python-Exercises)

- [Exercise Runner](#exercise-runner)
  * [Start a practice session](#start-a-practice-session)
  * [Get a new Exercise](#get-a-new-exercise)
  * [Testing your Solution](#testing-your-solution)
    + [Manually:](#manually-)
    + [Automated tests](#automated-tests)
  * [Submitting your solution](#submitting-your-solution)
  * [Common issues](#common-issues)

## Start a practice session
1. Open the terminal.
    - In the Repl.it window, press `ctrl + shift + s`.
2. Run `python -m exercise.start_session` in the terminal.

Practice sessions are designed to take 10-20 minutes and bring you through various important programming concepts a little bit at a time.

The concept behind a practice session is to eventually complete an ultimate (main goal) exercise by first completing various related "warm-up" exercises, whose concepts are already known to the programmer. The choice of warm up exercises will be informed by the programming concepts required to complete the main goal exercise.

The theory is, if the programmer gets stuck on the warm-up exercises, they might not be adequately prepared for the ultimate exercise. When a programmer notices a weakness in their skill-set, they can go back and practice exercises related to their weakness before returning to the regular progression of exercises.

In the normal course of your programming journey you will encounter the same programming problem multiple times. This is a good thing. Each time you complete the same problem, you will become more proficient at it and that process will help cement your understanding of that skill requirement for more difficult problems.


## Get a new Exercise
You can also choose to complete single exercises.

1. Open the terminal.
    - In the Repl.it window, press `ctrl + shift + s`.
2. Run `python -m exercise.get` in the terminal.
3. Select an exercise to attempt.
4. Any starter code will be written into the `main.py` file.
    - *Warning*: This will overwrite anything you may have had in there.
5. The instructions for the exercise will be found in `instructions.md`.
    - Be sure to hit the "Preview" button in the top right corner to view it with proper formatting.

## Testing your Solution
### Manually:
Hit "Run" at the top and manually test your program.

### Automated tests
1. Open the terminal.
    - In the Repl.it window, press `ctrl + shift + s`.
2. Run `pytest` in the terminal.
3. Outcomes:
    - **Failed**: if the tests fail, you will see *red text* and the output will let you know:
        - On what *line number* the error happend
        - What the difference was between your result and the expected result.
    - **Passed**: if the tests pass, you will see *green text*.
        - You can then move on to submit your solution

## Submitting your solution
1. Open the terminal.
    - In the Repl.it window, press `ctrl + shift + s`.
2. Run `python -m exercise.submit` in the terminal.
    - This will run the tests and submit the solution.
    - If the tests do not pass, you will be given the option to submit anyway.

## Common issues
#### When I type `pytest` in the terminal, it says `bash: pytest: command not found`.
- *Reason*: pytest has not yet been installed in the current repl environment
- *Solution*: In the terminal type `poetry install` or hit the "Run" button at the top.
#### When I type `pytest`, it says `NameError: name 'pytest' is not defined`.
- *Reason*: You are trying to run `pytest` in the Python shell. It is supposed to be run in the *Terminal*.
- *Solution*: Open the terminal with `ctrl + shift + s` and type `pytest` in the terminal.