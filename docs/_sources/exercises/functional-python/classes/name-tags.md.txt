# Name Tags



**Requirements:**
```eval_rst
- :ref:`fundamentals:__init__ method`
- :ref:`fundamentals:format output text`
- :ref:`fundamentals:returning a value`

```


There is a secret meeting of `The Agency: Scranton Branch` Agents. There will be juice, some fruit, and various little bite-sized cakes and treats. Because not all agents know each other, The Agency will be making name-tags for each Agent.

For security reasons, you have to **re-write** the `Agent` class. Do not copy and paste your previous code. You computer is most likely being monitored for copy-and-paste activity. You work for an intelligence agency, *The* Agency, afterall. Each offence could very well be logged and may result in consequences. You figure this is the perfect opportunity to absorb the content through repetition. You really want to keep this job. You're not so sure you're qualified to begin with.

```
Agent
=====
first_name: str
last_name: str
code_name: str
```

Because *The Agency* cares, they end up letting you bring your notebook around:

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

**MISSION**

Complete the `create_name_tag` function. Someone you intern under is enamoured with defining functions with perfect annotations and crisp docstrings, but leaves the more difficult work to you. You wonder if it should be the other way around but then realize how tedious annotations and docstrings are even though they look *sooooo* professional.

The `create_name_tag` function will take an `Agent` object and return a string (the name-tag) with the following format:

```
{first_name} {last_name}, {code_name|all caps}.
```

For example:

```
John Smith, HAPPY GHOST.
```

## Starter Code
```python
class Agent:
    # re-write the class
    pass


def create_name_tag(agent: Agent) -> str:
    """Creates a name-tag for an Agent.
    
    Args:
        agent: an Agent object
    Returns:
        The agent's name-tag.
    """
    pass
```

## Tests
```python
from main import Agent, create_name_tag


def test_john_smith_happy_ghost():
    happy_ghost = Agent("John", "Smith", "Happy Ghost")
    assert create_name_tag(happy_ghost) == "John Smith, HAPPY GHOST."


def test_jordan_peterson_misunderstood_professor():
    jbp = Agent("Jordan", "Peterson", "Misunderstood Professor")
    assert create_name_tag(jbp) == "Jordan Peterson, MISUNDERSTOOD PROFESSOR."


def test_simon_johnson_first_pope():
    peter = Agent("Simon", "Johnson", "First Pope")
    assert create_name_tag(peter) == "Simon Johnson, FIRST POPE."
```
