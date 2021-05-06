# Neutralization Pt. 3





OK, so now you remember **a)** how the `Agent` class stores `MissionReview` objects and **b)** how it calculates their latest-five mission average.

Before we can target the Agent's profile, we need to be able to do a search for the agent based on their various attributes. You need to update the agent class code to include the following:

1. An `all_agents` class-variable.

2. A `find_by_eye_color()` class-method or **static method**.

### Class-variable

In an object, the `self` pointer refers to one single object in particular. The `self` attributes are unique to the specific object. 

We can also store central data that pertains to the Class as a whole. In this case, we are going to store a class-variable called `all_agents`, which, will store all The Agency's agents. It will be a list that will be updated each time an `Agent` object is created.

Steps:

1. Fill in the blank at location `#1`. `all_agents` will be initialized as an empty list.

2. The last thing you do in the `__init__` method is append that newly created agent to the list of `all_agents`. The way you reference the list of `all_agents` from anywhere in the program is: `Agent.all_agents`. Append `self` to the list `all_agents`.

Run the tests at this point. The first two tests will verify what you just did. The other tests will fail, so don't be sad.

### Static Method

This is a method that applies to the `Agent` class as a whole. It does not operate on one `Agent` object in particular. As such, we don't have to pass `self` to it. We will just pass some `color` to it to search the list of `Agent.all_agents` and return a list of all matching agents.

In the `find_by_eye_color` static method, create a loop to run through `Agent.all_agents` and compare the given `color` to the `eye_color` of each `Agent` object. When you find a match, append that `Agent` to a list of matches.

Why am I helping you so much? You got yourself into this mess!

## Starter Code
```python
from typing import List


class Agent:
    _________ = __

    def __init__(self, first_name, last_name, eye_color, code_name):
        self.first_name = first_name
        self.last_name = last_name
        self.eye_color = eye_color
        self.code_name = code_name
        self.mission_reviews = []
        
    
    @staticmethod
    def find_by_eye_color(color: str) -> List["Agent"]:
        """Searches for all agents with the given eye_color.
        
        The method should find people whose eye color CONTAINS
        the search color. For example, when searching for "Blue" eyes, the
        method should find matches for both "Blue" eyes exactly
        any variation like "Icy-blue", or "Light blue" eyes.
        
        Args:
            color: The color. E.g., "Blue".
        
        Returns:
            A list of agents that match the given eye color.
            Empty list if no matches.
        """
        pass
```

## Tests
```python
import pytest

from main import Agent


@pytest.fixture(autouse=True)
def reset_class_variable():
    yield
    Agent.all_agents = []


def test_agent_class_has_class_variable_all_agents():
    assert Agent.all_agents == []


def test_agent_constructor_adds_new_agent_to_all_agents():
    new_agent = Agent("John", "Smith", "Blue", "Super Dude")
    assert new_agent in Agent.all_agents

    another_new_agent = Agent("Sally", "Johanson", "Red", "Strong Like Bull")
    assert another_new_agent in Agent.all_agents
    
    assert len(Agent.all_agents) == 2


def test_find_by_eye_color_empty_list():
    assert Agent.find_by_eye_color("no agents yet") == []


def test_find_by_eye_color_case_insensitive():
    colors = ['blue', 'blue', 'green', 'BLUE']

    agents = []
    for i, c in enumerate(colors):
        a = Agent("", "", c, "")
        agents.append(a)
    
    result_list = Agent.find_by_eye_color("blue")
    assert agents[0] in result_list
    assert agents[1] in result_list
    assert agents[2] not in result_list

    # The search should be case-insensitive
    assert agents[3] in result_list
    assert len(result_list) == 3


def test_find_by_eye_color_not_found_returns_empyt_list():
    colors = ['blue', 'blue', 'blue', 'blue']

    agents = []
    for i, c in enumerate(colors):
        a = Agent("", "", c, "")
        agents.append(a)
    
    result_list = Agent.find_by_eye_color("rainbow")
    assert result_list == []


def test_agent_find_by_eye_color_should_not_modify_all_agents_list():
    for _ in range(3):
        Agent("", "", "blue", "")
    
    result_list = Agent.find_by_eye_color("red")
    assert result_list == []

    # The algorithm should not remove agents
    # from Agent.all_agents
    assert len(Agent.all_agents) == 3
```
