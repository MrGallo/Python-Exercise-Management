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



