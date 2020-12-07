# Hangman Introduction



**Requirements:**
```eval_rst
- :ref:`fundamentals:storing data in variables`
- :ref:`fundamentals:format output text`
- :ref:`fundamentals:get input from the user`
- :ref:`fundamentals:convert to lower/upper case`
- :ref:`fundamentals:if, elif, else`
- :ref:`fundamentals:loop through a string (for)`
- :ref:`fundamentals:loop through a list (for)`
- :ref:`fundamentals:string building and filtering`
- :ref:`fundamentals:appending elements to a list`
- :ref:`fundamentals:check if a value is in a list`
- :ref:`fundamentals:defining a function`
- :ref:`fundamentals:returning a value`
- :ref:`fundamentals:defining parameters`
- :ref:`fundamentals:docstrings`

```


The purpose of this *Hangman* chapter is to give the programmer some practice working with and creating functions. You will be working on all the functions required to complete this particular game of *Hangman*. At the end, you will put together all the functions you created into one file and complete the entire program. Please see the requirements section for the knowledge covered for the whole series.

Our first task is to look over the `main` function for *Hangman* (shown below) and make note of what custom functions we will be responsible for creating. The task is complete when you print out the names of each custom function in the order they appear in the `main` function. One function name per line. Don't include the `print` function in your list, you will not be creating that. Also, you can leave out the parentheses, so just print out `get_random_word`, for example.

```python
def main():
    ATTEMPTS_ALLOWED = 6

    secret_word = get_random_word(WORD_LIST)

    correct_guesses = []
    incorrect_guesses = []
    lives = calc_attempts_remaining(ATTEMPTS_ALLOWED, incorrect_guesses)

    result = None
    while result is None:

        # display lives left
        print_lives_left(lives, ATTEMPTS_ALLOWED)

        # display hidden word
        blanked_word = reveal_letters(secret_word, correct_guesses)
        print(blanked_word)
        print()

        # get guess
        guess = get_guess(correct_guesses + incorrect_guesses)

        if letter_is_in_word(guess, secret_word):
            print("That is correct!")
            correct_guesses.append(guess)
        else:
            print("Incorect.")
            incorrect_guesses.append(guess)
        
        lives = calc_attempts_remaining(ATTEMPTS_ALLOWED, incorrect_guesses)
        
        if all_letters_present_in_list(secret_word, correct_guesses):
            result = "win"
        elif lives <= 0:
            result = "lose"

    print(word_reveal_message(secret_word))
    print(outcome_message(result))
```






## Tests
```python
def test_contains_function_names(capsys):
    names = """get_random_word
calc_attempts_remaining
print_lives_left
reveal_letters
get_guess
letter_is_in_word
calc_attempts_remaining
all_letters_present_in_list
word_reveal_message
outcome_message""".split("\n")

    import main
    captured = capsys.readouterr()
    for name in names:
        assert name in captured.out
```
