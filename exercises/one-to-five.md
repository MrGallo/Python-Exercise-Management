# One to Five

With the starter code (given in `main.py`) your program outputs an incomplete and out-of-order list of numbers. You goal is to fix it so it outputs the numbers from one to five.

1. Run the program and observe the incorrect output. It should start off as follows:
    ```
    three
    five
    four
    ```
    Notice that the strings `"one"` and `"two"` don't even show up. This is because those `print()` functions have been commented out using the pound-sign ("hashtag") and a space (`# `).
2. Remove the comment characters (pound-sign and the space) and allow the words "one" and "two" to show up. It should look like:
    ```
    three
    five
    one
    four
    two
    ```
    **Warning:** If you do not *also* delete the space, you will get an `IndentationError`. Make sure all the `p`'s in the word `print` are lined up with *no space* in front of them.
3. Rearrange the `print()` functions to correct the order of the words.
    ```
    one
    two
    three
    four
    five
    ```
