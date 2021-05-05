# The Interview



**Requirements:**
```eval_rst
- :ref:`fundamentals:unified modeling language (uml)`
- :ref:`fundamentals:__init__ method`

```


After studying for a couple minutes, you decided to call it a night and go to sleep.

In the morning, your phone rings and wakes you up. A call at this time wouldn't be so bad if you actually went to bed at a decent hour. The number is blocked, but something is telling you to answer it.

"Hello?"

"Greetings. You have been selected" a woman's voice greets you, a mixture of confidence and amusement, "to interview for a position in an elite intelligence agency."

"Wow! Like the CIA or the FBI?!" you excitedly exclaim. The woman scoffs and you wonder if perhaps you sound a bit *too* excited.

"Please. That's child's-play" responds the woman on the other line. She continues, "My superiors require you to prove your advanced programming capabilities by creating a `Person` class with a couple of specific attributes. Your failure to do so will prove to everyone your utter lack of capability. However, if you prove successful, you will be formally invited to join *The Agency*."

*The Agency*? She says it as though that's what the agency is actually called. You inwardly chuckle as you assure yourself that it couldn't possibly be the actual name of the agency. These intelligence types like to play it close to the chest. They wouldn't dare reveal to you the *real* name of the agency! Would they? At least not yet.

She continues to explain the specifications of the `Person` class as you grab a pen and a napkin (which happens to be stained by the pad thai sauce from last night's dinner).
You write out the specifications for the class in UML.

```
# the napkin.

Person
---------
name: str
age: int

# sauce stain -----> %$*(*&$*&())
```

You recognize that these attributes will have to be set by an `__init__` method referencing the `self` pointer.

You didn't study much, but thankfully, [StackOverflow](https://stackoverflow.com/) has your back and you find some nice [boilerplate for creating a class](https://stackoverflow.com/questions/8609153/why-do-we-use-init-in-python-classes/8609238#8609238).

## Starter Code
```python
class ______:
    def ________(____, _____, ___):
        self.name = ____
        self.age = ___
```

## Tests
```python
from main import Person


def test_can_create_person_object():
    p = Person("Jimmy", 10)
    assert type(p) is Person


def test_person_class_has_name_attribute_properly_assigned():
    p = Person("Jimmy", 10)
    assert p.name == "Jimmy"


def test_person_class_has_age_attribute_properly_assigned():
    p = Person("Jimmy", 10)
    assert p.age == 10


def test_person_acceptance():
    person = Person("Jimbo", 55)
    assert person.name == "Jimbo"
    assert person.age == 55
```
