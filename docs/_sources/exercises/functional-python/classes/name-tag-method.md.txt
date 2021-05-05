# Name Tag Method



**Requirements:**
```eval_rst
- :ref:`fundamentals:instance method`

```


```
MYSTERIOUS MESSAGE
From: UNKNOWN
To: You

The Agency hired you because they thought you knew
what you were doing. If they see the answer to your
last solution, you will be outed as a fraud. You must 
modify your noob code before they see it.

The function you made is outside of the Agent class.
You must convert that outside function to a "method"
INSIDE of the Agent class.

We must be able to access this method by saying:

agent.create_name_tag()

See how much nicer that looks?

Relax. Everything stays the same except the points
below. Follow my instructions exactly or else they
will find you out.

1. Indent the entire function so it falls under the
Agent class.

2. Remove the parameter variable and put the `self`
variable in there.

3. In the doc-string, remove the 'Args' section.

4. In the create_name_tag function body, you referenced
an agent object variable. Replace that with `self`.

I have rigged the system to replace your previous code
as soon as you pass all the tests I have provided.

I hope this reaches you in time.
- GL
```

## Starter Code
```python
class Agent:
    def __init__(self, first_name, last_name, code_name):
        self.first_name = first_name
        self.last_name = last_name
        self.code_name = code_name


def create_name_tag(agent: Agent) -> str:
    """Creates a name-tag for an Agent.
    
    Args:
        agent: an Agent object
    Returns:
        The agent's name-tag.
    """
    return "{} {}, {}.".format(agent.first_name,
                               agent.last_name,
                               agent.code_name.upper())
```

## Tests
```python
from main import Agent


def test_john_smith_happy_ghost():
    happy_ghost = Agent("John", "Smith", "Happy Ghost")
    assert happy_ghost.create_name_tag() == "John Smith, HAPPY GHOST."


def test_jordan_peterson_misunderstood_professor():
    jbp = Agent("Jordan", "Peterson", "Misunderstood Professor")
    assert jbp.create_name_tag() == "Jordan Peterson, MISUNDERSTOOD PROFESSOR."


def test_simon_johnson_first_pope():
    peter = Agent("Simon", "Johnson", "First Pope")
    assert peter.create_name_tag() == "Simon Johnson, FIRST POPE."
```
