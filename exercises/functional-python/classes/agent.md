# Agent



**Requirements:**
```eval_rst
- :ref:`fundamentals:unified modeling language (uml)`
- :ref:`fundamentals:__init__ method`

```


You have been accepted into *The Agency* (yes, thats *actually* what they call it) as an awesome hacker (intern). However, you cannot use "dark" theme in your IDE, yet. That is reserved for actual hackers.

The Agency needs you to start work on their new "Agent Program" program, for agents.

**Mission:** Create an `Agent` class as detailed in the UML below.

```
Agent
=====
first_name: str
last_name: str
code_name: str
```






## Tests
```python
from main import Agent


def test_agent_class_has_first_name_attribute_properly_assigned():
    agent = Agent("Jim", "Smith", "Fluffy Bunny")
    assert agent.first_name == "Jim"


def test_agent_class_has_last_name_attribute_properly_assigned():
    agent = Agent("Jim", "Smith", "Fluffy Bunny")
    assert agent.last_name == "Smith"


def test_agent_class_has_code_name_attribute_properly_assigned():
    agent = Agent("Jim", "Smith", "Fluffy Bunny")
    assert agent.code_name == "Fluffy Bunny"


def test_agent_acceptance():
    agent = Agent("David", "MacGyver", "Mr. Fixit")
    assert agent.first_name == "David"
    assert agent.last_name == "MacGyver"
    assert agent.code_name == "Mr. Fixit"
```
