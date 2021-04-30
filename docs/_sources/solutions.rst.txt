:orphan:

Solutions
=========

.. contents::
    :local:

Fundamentals
------------

introduction to programming
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Hello, World!
*************
.. code-block:: python
    :linenos:

    print("Hello,")
    print("World!")

Hello, Goodbye
**************
.. code-block:: python
    :linenos:

    print("Goodbye")
    

Hamburger
*********
.. code-block:: python
    :linenos:

    print("(--Bun--)")
    print("Hamburger")
    print("(--Bun--)")
    

One to Five
***********
.. code-block:: python
    :linenos:

    print("one")
    print("two")
    print("three")
    print("four")
    print("five")
    

Escape character
****************
.. code-block:: python
    :linenos:

    print("She said \"Hello\" to her friend.")
    print("Her friend said \"Nice to see you!\".")
    
    

Surface Area
************
.. code-block:: python
    :linenos:

    surface_area = 10 * 25
    print(f"The surface area is {surface_area} cm^2")
    

All the Operators
*****************
.. code-block:: python
    :linenos:

    print("One plus Two is:")
    print(1 + 2)
    
    print("Five minus Three is:")
    print(5 - 3)
    
    print("Six multiplied by Four is:")
    print(6 * 4)
    
    print("Twelve divided by Six is:")
    print(12 / 6)
    
    print("Twenty Three floor-divide by Five is:")
    print(23 // 5)
    
    print("The remainder of Twenty Three divided by Five is:")
    print(23 % 5)
    
    print("Two to the power of Eight is:")
    print(2 ** 8)

Student Groups
**************
.. code-block:: python
    :linenos:

    students = 33
    number_of_groups = 5
    
    students_per_group = students // number_of_groups
    students_left_over = students % number_of_groups
    
    print(f"If there are {students} students and {number_of_groups} groups.")
    print(f"There will be {students_per_group} students per group")
    print(f"and there will be {students_left_over} students without a group.")

How Many Quarters?
******************
.. code-block:: python
    :linenos:

    change_cents = 235
    quarters = change_cents // 25
    
    print(f"You will get back {quarters} quarters.")

Banquet Hall Chairs
*******************
.. code-block:: python
    :linenos:

    tables = 32
    chairs_per_table = 9
    
    # do not modify the code below this line
    total_chairs = tables * chairs_per_table
    print(f"There are {total_chairs} chairs.")


Functions
^^^^^^^^^
Execute order 66
****************
.. code-block:: python
    :linenos:

    def order_66():
        print("Executing Order 66:")
        print()
        print("Telling clones to attack the Jedi...")
        print("Assuming they will listen...")
        print("(apparently they had some bio-chip installed)")
        print("Most of the Jedi have been eliminated.")
        print("... except those Jedi that would provide convenient successive expanded-universe story-lines.")
    
    
    order_66()

Hello, goodbye
**************
.. code-block:: python
    :linenos:

    def hello_goodbye():
        print("Hello,")
        print("goodbye.")
    
    
    hello_goodbye()
    hello_goodbye()
    hello_goodbye()
    hello_goodbye()

Opening arguments
*****************
.. code-block:: python
    :linenos:

    def give_argument(argument: str) -> None:
        print("The defense will commence with their opening arguments:")
        print(f"Your Honour, {argument}.")
    
    
    give_argument("my client is innocent")

Do my homework
**************
.. code-block:: python
    :linenos:

    def get_friend_to_do_your_homework(subject: str, chapter: str) -> None:
        print(f"Ok, I'll complete the {chapter} chapter of your {subject} work.")
    
    
    get_friend_to_do_your_homework("math", "functions")

The Answer
**********
.. code-block:: python
    :linenos:

    def get_answer_to_everything() -> int:
        return 42
    
    
    answer = get_answer_to_everything()
    print(f"The answer to life is {answer}.")

Print Banner
************
.. code-block:: python
    :linenos:

    def print_banner():
        print("  _    _      _ _         __          __        _     _ _ ")
        print(" | |  | |    | | |        \ \        / /       | |   | | |")
        print(" | |__| | ___| | | ___     \ \  /\  / /__  _ __| | __| | |")
        print(" |  __  |/ _ \ | |/ _ \     \ \/  \/ / _ \| '__| |/ _` | |")
        print(" | |  | |  __/ | | (_) |     \  /\  / (_) | |  | | (_| |_|")
        print(" |_|  |_|\___|_|_|\___( )     \/  \/ \___/|_|  |_|\__,_(_)")
        print("                      |/                                  ")

FITB Average
************
.. code-block:: python
    :linenos:

    def calc_average(numbers):
        return sum(numbers) / len(numbers)

Skyline
*******
.. code-block:: python
    :linenos:

    def building_a():
        print("-----------")
        print("**********|")
        print("**********|")
        print("-----------")
    
    
    def building_c():
        print("--------")
        print("' '' ''|")
        print("--------")
    
    
    def building_b():
        print("###############")
        print("###############")
        
    
    building_a()
    building_c()
    building_b()
    building_a()
    building_c()
    building_c()

The Number N
************
.. code-block:: python
    :linenos:

    def the_number_two():
        return 2
    
    
    def the_number_three():
        return 3
    
    
    
    the_sum = the_number_two() + the_number_three()
    the_product = the_number_two() * the_number_three()
    
    print(the_sum)  # should be 5
    print(the_product)  # should be 6

Mystery Numbers
***************
.. code-block:: python
    :linenos:

    def mystery_number_a():
        return 8
    
    
    def mystery_number_b():
        return 2

Perimeter Parameter
*******************
.. code-block:: python
    :linenos:

    def side_length_from_perimeter(perimeter: float) -> float:
        """Get the side length of a square by its perimeter.
        
        Args:
            perimeter (float): The perimiter of the square.
        
        Returns:
            The side length of the square.
        """
        return perimeter / 4

String Times
************
.. code-block:: python
    :linenos:

    def string_times(string: str, n: int) -> str:
        """Get a string repeated n times."""
        new_string = ""
        for i in range(n):
            new_string += string
        return new_string



Practical Programming
---------------------

Hangman
^^^^^^^
Hangman Introduction
********************
.. code-block:: python
    :linenos:

    print("get_random_word")
    print("calc_attempts_remaining")
    print("print_lives_left")
    print("reveal_letters")
    print("get_guess")
    print("letter_is_in_word")
    print("calc_attempts_remaining")
    print("all_letters_present_in_list")
    print("word_reveal_message")
    print("outcome_message")

Choosing the secret word
************************
.. code-block:: python
    :linenos:

    from typing import List
    
    import random
    
    
    def get_random_word(word_list: List[str]) -> str:
        """Gets a random word.
        
        Args: 
            word_list: the list from which to get the word.
        
        Returns:
            A single word.
        """
        return random.choice(word_list)

Calculating remaining attempts
******************************
.. code-block:: python
    :linenos:

    from typing import List
    
    
    def calc_attempts_remaining(attempts_allowed: int, incorrect: List[str]) -> int:
        """Determine the number of guesses remaining.
    
        Based on the initial number of allowed attempts and the number
        of incorrect guesses.
        
        Args:
            attempts_allowed: The number of total allowed guesses.
            incorrect: A list containing all the incorrect guesses.
        
        Returns:
            How many remaining guesses the player has.
        """
        return attempts_allowed - len(incorrect)

Hide or reveal letters
**********************
.. code-block:: python
    :linenos:

    from typing import List
    
    
    def reveal_letters(word: str, visible_letters: List[str]) -> str:
        """Reveal the given letters in a hidden word.
        
        Args:
            word: The word whose letters need to be revealed.
            visible_letters: A list of letters that should be visible in the word.
        
        Returns:
            The word with visible letters shown and all others blanked-out.
        
        Example:
            If the word is "hello" and visible_letters is the list ['e', 'o'],
            The resulting string would be "_ e _ _ o". Separate each character
            with a space to make it easier to read.
        """
        new_string = ""
        for c in word:
            if c in visible_letters:
                new_string += c + " "
            else:
                new_string += "_ "
    
        return new_string.strip()

Word reveal
***********
.. code-block:: python
    :linenos:

    def word_reveal_message(word: str) -> str:
        """Creates a message revealing the secret word.
        
        Args:
            word: the word being revealed.
        
        Returns:
            A message revealing the secret word.
        
        Example: 
            "The secret word was 'orange'."
        """
        return f"The secret word was'{word}'"

Outcome message
***************
.. code-block:: python
    :linenos:

    def outcome_message(result: str) -> str:
        """Creates a message based on the player's outcome.
        
        Args:
            result: Either 'win' or 'lose'.
        
        Returns:
            An appropriate message based on the player's outcome.
        """
        if result == "win":
            return "Congratulations! You won!"
        else:
            return "Sorry. You lost."



Codingbat
---------

Warmup-1
^^^^^^^^
front_back
**********
.. code-block:: python
    :linenos:

    def repeat_front(string: str, n: int) -> str:
        new_string = ""
        slice_size = n
        while slice_size > 0:
            new_string += string[0:slice_size]
            slice_size -= 1
    
        return new_string


String-1
^^^^^^^^

String-2
^^^^^^^^
double_char
***********
.. code-block:: python
    :linenos:

    def double_char(string: str) -> str:
    
        new_string = ""
        for c in string:
            new_string += c + c
    
        return new_string

count_hi
********
.. code-block:: python
    :linenos:

    def count_hi(string: str) -> int:
        hi_count = 0
        i = 0
        while i < len(string) - 1:
            if string[i:i+2] == "hi":
                hi_count += 1
            
            i += 1
        
        return hi_count

cat_dog
*******
.. code-block:: python
    :linenos:

    def cat_dog(string: str) -> bool:
        cat_count = 0
        dog_count = 0
    
        i = 0
        while i < len(string) - 2:
            substring = string[i:i+3]
            if substring == "cat":
                cat_count += 1
            elif substring == "dog":
                dog_count += 1
            i += 1
    
        return cat_count == dog_count

count_code
**********
.. code-block:: python
    :linenos:

    def count_code(string: str) -> int:
        count = 0
        i = 0
        while i < len(string) - 3:
            if string[i:i+2] == "co" and string[i+3] == "e":
                count += 1
            i += 1
    
        return count

end_other
*********
.. code-block:: python
    :linenos:

    def end_other(a: str, b: str) -> bool:
        a = a.lower()
        b = b.lower()
    
        if a[-len(b):] == b:
            return True
        elif b[-len(a):] == a:
            return True
        else:
            return False

xyz_there
*********
.. code-block:: python
    :linenos:

    def xyz_there(string: str) -> bool:
        i = 0
        while i < len(string) - 2:
            if string[i] == ".":
                i += 2
            else:
                if string[i:i+3] == "xyz":
                    return True
                i += 1
    
        return False

bob_there
*********
.. code-block:: python
    :linenos:

    def bob_there(string: str) -> bool:
        i = 0
        while i < len(string) - 2:
            if string[i] == "b" and string[i+2] == "b":
                return True
            i += 1
    
        return False

xy_balance
**********
.. code-block:: python
    :linenos:

    def xy_balance(string: str) -> bool:
        found_y = False
        i = len(string) - 1
        while i >= 0:
            if string[i] == "y":
                found_y = True
            elif string[i] == "x":
                if not found_y:
                    return False
                break
            i -= 1
    
        return True

mix_string
**********
.. code-block:: python
    :linenos:

    def mix_string(a: str, b: str) -> str:
        new_string = ""
        i = 0
        while i < len(a) and i < len(b):
            new_string += a[i] + b[i]
            i += 1
    
        new_string += a[i:]
        new_string += b[i:]
    
        return new_string

repeat_end
**********
.. code-block:: python
    :linenos:

    def repeat_end(string: str, n: int) -> str:
        new_string = ""
        i = 0
        while i < n:
            new_string += string[-n:]
            i += 1
    
        return new_string

repeat_separator
****************
.. code-block:: python
    :linenos:

    def repeat_separator(word: str, sep: str, count: int) -> str:
        new_string = ""
        i = 0
        while i < count:
            if i > 0:
                new_string += sep
            new_string += word
            i += 1
    
        return new_string

prefix_again
************
.. code-block:: python
    :linenos:

    def prefix_again(string: str, n: int) -> bool:
        prefix = string[:n]
        i = n
        while i < len(string) - (n - 1):
            if string[i:i+n] == prefix:
                return True
            i += 1
    
        return False

xyz_middle
**********
.. code-block:: python
    :linenos:

    def xyz_middle(string: str) -> bool:
        clip = (len(string) - 3) // 2
        clipped = string[clip:len(string)-clip]
        return "xyz" in clipped


List-1
^^^^^^
common_end
**********
.. code-block:: python
    :linenos:

    from typing import List
    
    
    def common_end(a: List[int], b: List[int]) -> bool:
        if a[0] == b[0]:
            return True
        elif a[-1] == b[-1]:
            return True
        else:
            return False

max_end_3
*********
.. code-block:: python
    :linenos:

    from typing import List
    
    
    def max_end_3(nums: List[int]) -> List[int]:
        first = nums[0]
        last = nums[-1]
    
        if first > last:
            return [first, first, first]
        else:
            return [last, last, last]


List-2
^^^^^^
count_evens
***********
.. code-block:: python
    :linenos:

    from typing import List
    
    
    def count_evens(nums: List[int]) -> int:
        evens = 0
        for n in nums:
            if n % 2 == 0:
                evens += 1
        return evens

big_diff
********
.. code-block:: python
    :linenos:

    from typing import List
    
    
    def big_diff(nums: List[int]) -> int:
        largest = nums[0]
        smallest = nums[0]
        
        for n in nums:
            if n > largest:
                largest = n
            elif n < smallest:
                smallest = n
        
        return largest - smallest

fizz_array
**********
.. code-block:: python
    :linenos:

    from typing import List
    
    
    def fizz_array(n: int) -> List[int]:
        new_list = []
        i = 0
        while i < n:
            new_list.append(i)
            i += 1
    
        return new_list

fizz_buzz
*********
.. code-block:: python
    :linenos:

    from typing import List
    
    
    def fizz_buzz(start: int, end: int) -> List[str]:
        new_list = []
        i = start
        while i < end:
            if i % 3 == 0 and i % 5 == 0:
                new_list.append("FizzBuzz")
            elif i % 3 == 0:
                new_list.append("Fizz")
            elif i % 5 == 0:
                new_list.append("Buzz")
            else:
                new_list.append(str(i))
            i += 1
        
        return new_list



Codingbat (Input/Output)
------------------------

Warmup-1
^^^^^^^^

String-1
^^^^^^^^

String-2
^^^^^^^^
double_char
***********
.. code-block:: python
    :linenos:

    string = input()
    
    new_string = ""
    for c in string:
        new_string += c + c
    
    print(new_string)

count_hi
********
.. code-block:: python
    :linenos:

    string = input()
    
    hi_count = 0
    i = 0
    while i < len(string) - 1:
        if string[i:i+2] == "hi":
            hi_count += 1
    
        i += 1
    
    print(hi_count)

cat_dog
*******
.. code-block:: python
    :linenos:

    string = input()
    
    cat_count = 0
    dog_count = 0
    
    i = 0
    while i < len(string) - 2:
        substring = string[i:i+3]
        if substring == "cat":
            cat_count += 1
        elif substring == "dog":
            dog_count += 1
        i += 1
    
    if cat_count == dog_count:
        print("True")
    else:
        print("False")

count_code
**********
.. code-block:: python
    :linenos:

    string = input()
    
    count = 0
    
    i = 0
    while i < len(string) - 3:
        if string[i:i+2] == "co" and string[i+3] == "e":
            count += 1
        i += 1
    
    print(count)

end_other
*********
.. code-block:: python
    :linenos:

    str_1 = input().lower()
    str_2 = input().lower()
    
    if str_1[-len(str_2):] == str_2:
        print("True")
    elif str_2[-len(str_1):] == str_1:
        print("True")
    else:
        print("False")

xyz_there
*********
.. code-block:: python
    :linenos:

    string = input()
    
    contains_xyz = "False"
    i = 0
    while i < len(string) - 2:
        if string[i] == ".":
            i += 2
        else:
            if string[i:i+3] == "xyz":
                contains_xyz = "True"
            i += 1
    
    print(contains_xyz)

bob_there
*********
.. code-block:: python
    :linenos:

    string = input()
    
    contains_bob = "False"
    i = 0
    while i < len(string) - 2:
        if string[i] == "b" and string[i+2] == "b":
            contains_bob = "True"
            break
        i += 1
    
    print(contains_bob)

xy_balance
**********
.. code-block:: python
    :linenos:

    string = input()
    
    balanced = True
    found_y = False
    i = len(string) - 1
    while i >= 0:
        if string[i] == "y":
            found_y = True
        elif string[i] == "x":
            if not found_y:
                balanced = False
            break
    
        i -= 1
    
    print(balanced)

mix_string
**********
.. code-block:: python
    :linenos:

    a = input()
    b = input()
    
    new_string = ""
    i = 0
    while i < len(a) and i < len(b):
        new_string += a[i] + b[i]
        i += 1
    
    new_string += a[i:]
    new_string += b[i:]
    
    print(new_string)

repeat_end
**********
.. code-block:: python
    :linenos:

    string = input()
    n = int(input())
    
    new_string = ""
    i = 0
    while i < n:
        new_string += string[-n:]
        i += 1
    
    print(new_string)

repeat_front
************
.. code-block:: python
    :linenos:

    string = input()
    n = int(input())
    
    new_string = ""
    slice_size = n
    while slice_size > 0:
        new_string += string[0:slice_size]
        slice_size -= 1
    
    print(new_string)

repeat_separator
****************
.. code-block:: python
    :linenos:

    word = input()
    sep = input()
    count = int(input())
    
    new_string = ""
    i = 0
    while i < count:
        new_string += word
        i += 1
        if i != count:  # if it's not the last loop
            new_string += sep
    
    print(new_string)

prefix_again
************
.. code-block:: python
    :linenos:

    string = input()
    n = int(input())
    
    again = False
    prefix = string[:n]
    i = n
    while i < len(string) - (n - 1):
        if string[i:i+n] == prefix:
            again = True
            break
        i += 1
    
    print(again)

xyz_middle
**********
.. code-block:: python
    :linenos:

    string = input()
    
    clip = (len(string) - 3) // 2
    clipped = string[clip:len(string)-clip]
    if "xyz" in clipped:
        print(True)
    else:
        print(False)



Dynamic Programming
-------------------

Memoization
^^^^^^^^^^^
Fibonacci
*********
.. code-block:: python
    :linenos:

    from typing import Dict, Optional
    
    
    def fib(n: int, memo: Optional[Dict[int, int]] = None) -> int:
        if memo is None:
            memo = {}
        
        if n in memo.keys():
            return memo[n]
    
        if n <= 2:
            return 1
        
        memo[n] = fib(n-2, memo) + fib(n-1, memo)
        return memo[n]

Grid Traveler
*************
.. code-block:: python
    :linenos:

    from typing import Dict
    
    
    def grid_traveler(m: int, n: int, memo: Dict = None) -> int:
        if memo is None:
            memo = {}
        
        key = (m, n)
        if key in memo.keys():
            return memo[key]
        
        if m == 0 or n == 0:
            return 0
        
        if m == 1 and n == 1:
            return 1
    
        memo[key] = grid_traveler(m-1, n, memo) + grid_traveler(m, n-1, memo)
        return memo[key]

Can Sum
*******
.. code-block:: python
    :linenos:

    from typing import List, Dict
    
    
    def can_sum(target_sum: int, numbers: List[int], memo: Dict = None):
        if memo is None:
            memo = {}
        
        if target_sum in memo.keys():
            return memo[target_sum]
    
        if target_sum == 0:
            return True
        elif target_sum < 0:
            return False
        
        for n in numbers:
            difference = target_sum - n
            if can_sum(difference, numbers, memo):
                memo[target_sum] = True
                return True
        
        memo[target_sum] = False
        return False

How Sum
*******
.. code-block:: python
    :linenos:

    from typing import List, Dict
    
    
    def how_sum(target_sum: int, numbers: List[int], memo: Dict = None) -> List[int]:
        if memo is None:
            memo = {}
        
        if target_sum in memo.keys():
            return memo[target_sum]
    
        if target_sum == 0:
            return []
        elif target_sum < 0:
            return None
        
        for n in numbers:
            difference = target_sum - n
            result = how_sum(difference, numbers, memo)
            if result is not None:
                memo[target_sum] = [n] + result
                return memo[target_sum]
        
        memo[target_sum] = None
        return None

Best Sum
********
.. code-block:: python
    :linenos:

    from typing import List, Dict
    
    
    def best_sum(target_sum: int, numbers: List[int], memo: Dict = None) -> List[int]:
        if memo is None:
            memo = {}
        
        if target_sum in memo.keys():
            return memo[target_sum]
        
        if target_sum == 0:
            return []
        elif target_sum < 0:
            return None
    
        shortest = None
        for n in numbers:
            difference = target_sum - n
            result = best_sum(difference, numbers, memo)
            if result is not None:
                combo = [n] + result
                if shortest is None or len(combo) < len(shortest):
                    shortest = combo
        
        memo[target_sum] = shortest
        return shortest

Can Construct
*************
.. code-block:: python
    :linenos:

    from typing import List, Dict
    
    
    def can_construct(target: str, wordbank: List[str], memo: Dict = None) -> bool:
        if memo is None:
            memo = {}
        
        if target in memo.keys():
            return memo[target]
    
        if target == "":
            return True
        
        for word in wordbank:
            if target.startswith(word):
                remaining = target[len(word):]
                if can_construct(remaining, wordbank, memo):
                    memo[target] = True
                    return True
    
        memo[target] = False
        return False

Count Construct
***************
.. code-block:: python
    :linenos:

    from typing import List, Dict
    
    
    def count_construct(target: str, wordbank: List[str], memo: Dict = None) -> int:
        if memo is None:
            memo = {}
        
        if target in memo.keys():
            return memo[target]
    
        if target == "":
            return 1
        
        count = 0
        for word in wordbank:
            if target.startswith(word):
                remaining = target[len(word):]
                count += count_construct(remaining, wordbank, memo)
        
        memo[target] = count
        return count

All Construct
*************
.. code-block:: python
    :linenos:

    from typing import List, Dict
    
    
    def all_construct(target: str, wordbank: List[str], memo: Dict = None) -> List[List[str]]:
        if memo is None:
            memo = {}
        
        if target in memo.keys():
            return memo[target]
    
        if target == "":
            return [[]]
        
        combinations = []
        for word in wordbank:
            if target.startswith(word):
                remaining = target[len(word):]
                sub_combinations = all_construct(remaining, wordbank, memo)
                combinations += [[word] + c for c in sub_combinations]
    
        memo[target] = combinations
        return combinations



CCC Problems
------------

Junior 2020
^^^^^^^^^^^


Functional Python
-----------------

Intro
^^^^^
f(x) = x + 4
************
.. code-block:: python
    :linenos:

    def f(x: int) -> int:
        """Returns the value of x plus 4
        
        Args:
            x: An integer
        Returns:
            Another integer, x + 4
        """
        return x + 4

say_hello
*********
.. code-block:: python
    :linenos:

    def say_hello(name: str) -> str:
        """Creates a greeting for a friend.
        
        Args:
            name: The name of someone to say hi to
        Returns:
            A greeting in the format "Hello, {name}!"
        """
        return f"Hello, {name}!"

Sum of three numbers
********************
.. code-block:: python
    :linenos:

    def add(a: int, b: int, c: int) -> int:
        """Returns the sum of three integers.
        
        Args:
            a: a number
            b: a number
            c: a number
        Returns:
            Sum of the numbers
        """
        return a + b + c


Lists
^^^^^
Empty List
**********
.. code-block:: python
    :linenos:

    from typing import List
    
    
    def get_empty_list() -> List:
        """Returns an empty list"""
        return []

Pi List
*******
.. code-block:: python
    :linenos:

    from typing import List
    
    
    def get_pi() -> List[int]:
        """Returns the first three digits of Pi in a list"""
        return [3, 1, 4]

sum
***
.. code-block:: python
    :linenos:

    def sum_list(numbers: List[float]) -> float:
        """Returns the sum of a list of numbers.
    
        Args:
            numbers: A list of float numbers.
        Returns:
            The sum of the numbers.
        
        Note: Do NOT use the sum() built-in function to 
              accomplish this. Use a loop.
        """
        total = 0
        for n in numbers:
            total += n
        
        return total

Sum Even
********
.. code-block:: python
    :linenos:

    def sum_even(numbers: List[int]) -> int:
        """Returns the sum all even numbers in a list.
    
        Args:
            numbers: A list of integers.
        Returns:
            The sum of the even integers.
        
        Note: Use modulus (%) to discover even integers.
        """
        total = 0
        for n in numbers:
            if n % 2 == 0:
                total += n
        
        return total

Sum even and 7
**************
.. code-block:: python
    :linenos:

    from typing import List
    
    
    def sum_even_and_7(numbers: List[int]) -> int:
        """Returns the sum all even numbers, and 7's, in a list.
    
        Args:
            numbers: A list of integers.
        Returns:
            The sum of the even integers, including all 7's.
        
        Note: Use modulus (%) to discover even integers.
        """
        total = 0
        for num in numbers:
            if num % 2 == 0 or num == 7:
                total += num
        
        return total

Sum even and next neighbour
***************************
.. code-block:: python
    :linenos:

    from typing import List
    
    
    def sum_even_and_next_neighbour(numbers: List[int]) -> int:
        """Returns the sum all even numbers and their next neighbour.
    
        Args:
            numbers: A list of integers.
        Returns:
            The sum of the even integers, including next neighbours of even numbers.
        """
        total = 0
        i = 0
        while i < len(numbers):
            num = numbers[i]
            if num % 2 == 0:
                total += num
    
                if i + 1 < len(numbers):  # if there is a "next neighbour"
                    neighbour = numbers[i + 1]
                    total += neighbour
                    i += 1
           
            i += 1
            
        return total

Scary 13
********
.. code-block:: python
    :linenos:

    from typing import List
    
    
    def sum_scary_13(numbers: List[int]) -> int:
        """Returns the sum all numbers jumping over 13 and the next number.
    
        Args:
            numbers: A list of integers.
        Returns:
            The sum of all numbers, not including 13 and it's next neighbour.
        """
        total = 0
        i = 0
    
        while i < len(numbers):
            num = numbers[i]
    
            if num == 13:
                i += 2
            else:
                total += num
                i += 1
        
        return total


Dictionaries
^^^^^^^^^^^^
Empty Dict
**********
.. code-block:: python
    :linenos:

    from typing import Dict
    
    
    def create_an_empty_dictionary() -> Dict:
        """Creates an empty dictionary
        
        Args: 
            None
        Returns:
            Empty dictionary
        """
        return {}

Create Person
*************
.. code-block:: python
    :linenos:

    from typing import Dict
    
    
    def create_person_dict(first_name: str, last_name:str) -> Dict:
        """Creates a person dictionary with the given first and last name.
        
        Args:
            first_name: The person's first name
            last_name: The person's last name
        Returns:
            Person represented as a dictionary
            with keys "first_name" and "last_name".
        """
        return {
            "first_name": first_name,
            "last_name": last_name
        }

Get First Name
**************
.. code-block:: python
    :linenos:

    from typing import Dict
    
    
    def get_first_name(person: Dict[str, str]) -> str:
        """Returns the first name from a person dict
        
        Args:
            person: The person dict
                    The dictionary has the keys 'first_name' and 'last_name'.
        Returns:
            The person's first name
        """
        return person["first_name"]

Reverse Last Name
*****************
.. code-block:: python
    :linenos:

    from typing import Dict
    
    
    def reverse_last_name(person: Dict[str, str]) -> str:
        """Gets the person's last name reversed
        Args:
            person: Person dict with first and last name.
                    The dictionary has the keys 'first_name' and 'last_name'.
        Returns:
            Last name reversed and capitalized
        """
        last_name = person["last_name"]
        last_name_reversed = last_name[::-1]
        return last_name_reversed.capitalize()

Potentially Explosive
*********************
.. code-block:: python
    :linenos:

    from typing import Dict
    
    
    def is_potentially_explosive(inventory: Dict) -> bool:
        """Determines if your inventory is potentially explosive.
        
        An inventory is considered potentially explosive if it contains
        even the mention of both "fire" and "propane" in the dictionary's keys.
        The quantities of each element are irrevelant.
        
        Args:
            inventory: A dictionary that may be explosive.
        Returns:
            True if potentially explosive, False otherwise.
        """
        fire_mentioned = "fire" in inventory
        propane_mentioned = "propane" in inventory
        
        return fire_mentioned and propane_mentioned

Keys with Target
****************
.. code-block:: python
    :linenos:

    from typing import Dict, List
    
    
    def get_keys_with(target: str, thing: Dict[str, str]) -> List[str]:
        """Returns a list of keys in a dict which contain the target string.
        Args:
            target (str): The target substring to look for.
            thing (dict): A dictionary whose keys we want to search.
        Returns:
            (list) A list of all keys in the dictionary that contain the 
            target substring.
        """
        found_keys = []
        for key in thing.keys():
            if target in key:
                found_keys.append(key)
        
        return found_keys

Values Above Ten
****************
.. code-block:: python
    :linenos:

    from typing import Dict, List
    
    
    def values_above_10(inventory: Dict[str, int]) -> List:
        """Gives a list of dictionary values greater than 10.
        
        Args:
            inventory: Dictionary of inventory-like key value pairs.
        Returns:
            List of values (not keys) from the dictionary above 10.
    
        """
        target_values = []
        for key, value in inventory.items():
            if value > 10:
                target_values.append(value)
        
        return target_values

Above Average
*************
.. code-block:: python
    :linenos:

    from typing import List, Dict
    
    
    def students_above_average(student_final_marks: Dict[str, int]) -> List[str]:
        """Get a list of all student names whose mark is above average.
    
        Args:
            student_final_marks: A dictionary mapping student names to final marks.
        
        Returns:
            A list of student names.
        """
        # find average
        total = 0
        for mark in student_final_marks.values():
            total += mark
        
        average = total / len(student_final_marks.values())
    
        # filter students into a new list
        student_names = []
        for name, mark in student_final_marks.items():
            if mark > average:
                student_names.append(name)
        
        return student_names

Shopping List
*************
.. code-block:: python
    :linenos:

    from typing import List, Dict
    
    
    def get_shopping_list(inventory: Dict[str, int], minimum_stock: Dict[str, int]) -> List[str]:
        """Get a list of all items that are below the minimum stock threshold.
    
        Args:
            inventory: A dictionary mapping item names to current stock levels.
            minimum_stock: A dictionary mapping item names to their lowest allowed stock levels.
    
        Returns:
            A list of item names that need to be purchased. These are items
            whose stock levels are below their respective minimum stock threshold.
        """
        items = []
        for item, current_stock in inventory.items():
            if current_stock < minimum_stock[item]:
                items.append(item)
        
        return items


File R/W
^^^^^^^^
Get Contents
************
.. code-block:: python
    :linenos:

    def get_contents() -> str:
        with open("file.txt", "r") as f:
            contents = f.read()
        
        return contents

Variable Filename
*****************
.. code-block:: python
    :linenos:

    def get_contents(file_name: str) -> str:
        """Returns the contents of the given file.
        
        Args:
            file_name: The name of the file to fetch the contents.
        Returns:
            The contents of the given file as a string.
        """
        with open(file_name, "r") as f:
            contents = f.read()
        return contents

Friendly File
*************
.. code-block:: python
    :linenos:

    def friendly_mean_or_neutral(file_name: str) -> str:
        """Determines if a file is friendly, mean, or neutral.
        
        Args:
            file_name: The name of the file to check.
        Returns:
            "friendly", "mean" or "neutral" depending on the contents.
        """
        with open(file_name, "r") as f:
            contents = f.read()
        
        if contents in ["hello", "hi", "howdy"]:
            return "friendly"
        elif contents in ["boo", "leave", "blah"]:
            return "mean"
        else:
            return "neutral"

Write to File
*************
.. code-block:: python
    :linenos:

    def write_to_file():
        """Writes "Hello, file!" to a file called "file.txt."""
        
        with open("file.txt", "w") as f:
            f.write("Hello, file!")

Write Message to File
*********************
.. code-block:: python
    :linenos:

    def write_msg_to_file(msg: str, file_name: str) -> None:
        """Will write a message to a file
        
        Args:
            msg: The message to write.
            file_name: The name of the file to write the message in.
        """
        with open(file_name, "w") as f:
            f.write(msg)

Update High Score
*****************
.. code-block:: python
    :linenos:

    def check_and_update_high_score(current_score: int) -> None:
        """Updates the high score file if the current score is larger.
        
        Args:
            current_score: The score of the game that just ended.
        """
        with open('high_score.txt', 'r') as f:
            high_score = int(f.read())
        
        if current_score > high_score:
            with open('high_score.txt', 'w') as f:
                f.write(str(current_score))

Read Multiple Lines
*******************
.. code-block:: python
    :linenos:

    def add_nums_from_file(file_name: str) -> int:
        """Returns the sum of all integers in the given file.
        
        Args:
            file_name: The name of the file.
        Returns:
            Sum of all the numbers in the file.
        """
        total = 0
        with open(file_name, "r") as f:
            for line in f:
                total += int(line)
        
        return total

Load Code Name
**************
.. code-block:: python
    :linenos:

    import json
    
    
    def extract_code_name(file_name: str) -> str:
        """Extracts the operative's code name from a JSON file.
        
        Args:
            file_name: The name of the file with the operative's information.
        Returns:
            The operative's code name. The dictionary loaded from the JSON
            file will have a key of "code_name".
        """
        with open(file_name, "r") as f:
            agent_dict = json.load(f)
        
        code_name = agent_dict["code_name"]
        return code_name

Generate Code Name
******************
.. code-block:: python
    :linenos:

    import json
    
    
    def generate_code_name(file_name: str) -> str:
        """Generates a code-name using information within the file of an operative.
        
        Args:
            file_name: The name of the operative's secret file.
            The file contains a JSON representation of the operative.
            See the "Dictionary Specification" section in the description.
            
        Returns:
            A generated code-name for the operative.
        """
        adjective_map = {
            "White": "Happy",
            "Blue": "Sad",
            "Red": "Angry",
            "Pink": "Manly"
        }
    
        with open(file_name, "r") as f:
            operative = json.load(f)
        
        # ADJECTIVE
        fav_color = operative["fav_color"]
        adjective = adjective_map[fav_color]
    
        # NOUN
        score = operative["academy_score"]
        if score >= 90:
            noun = "Beast"
        elif score >= 80:
            noun = "Warlock"
        elif score >= 70:
            noun = "Mountain"
        elif score >= 60:
            noun = "Guppy"
        elif score >= 50:
            noun = "Sloth"
        else:
            noun = "Dropout"
        
        return f"{adjective} {noun}"



