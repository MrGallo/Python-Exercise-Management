# Neutralization Pt. 2



**Requirements:**
```eval_rst
- :ref:`fundamentals:__init__ method`
- :ref:`fundamentals:accessing object attributes`
- :ref:`fundamentals:loop through a list of objects`
- :ref:`fundamentals:slicing a list`
- :ref:`fundamentals:loop with an accumulator variable`

```


The second problem is you don't remember the modifications you wrote for the Agent class (you copy-and-pasted too much from [Stack Overflow](https://stackoverflow.com/)). 

You remember adding a `self.mission_reviews: List[MissionReview]` field. Every agent has a long list of `MissionReview` objects. In those mission reviews are the mission review grades you need to modify to neutralize the troublesome agent using your computer skills.

```
MissionReview
=============
mission_name: str
agent_code_name: str
grade: int
text: str
```

**First**

Add the `self.mission_reviews` field to the `Agent` class and give it an **empty list**. This is NOT something that should be passed as an argument to the init method. But, you knew that. Right? How can an agent have mission reviews before they are even added to the "Agent Program" program, for agents? They were *just* hired! PUT AN EMPTY LIST!

```
Agent
=====
first_name: str
last_name: str
code_name: str
mission_reviews: List[MissionReview]
-------
`calc_performance_rating(self) -> float`
```

**Second**

You also added a `calc_performance_rating()` instance method to the `Agent` class. Again, you copy-and-pasted way too much and must try to remember what you put there. Complete the function, for practice.

See the docstring for more info.

## Starter Code
```python
class Agent:
    def __init__(self, first_name, last_name, code_name):
        self.first_name = first_name
        self.last_name = last_name
        self.code_name = code_name
        ____._______________ = []
    
    
    def _____________________(____) -> ____:
        """Calculates average Mission Review preformance grade (last five).
        
        Returns:
            The average grade (float) of the Agent's 
            last five mission review grades.

            Returns None if there are no reviews.
            
        Hints:
            1. Use list slicing to get the last 5 elements.
               e.g., marks[-2:] gets the last two
            2. When you find the average don't forget
               that the original list might not even
               have 5 reviews in it.
        """
        pass
```

## Tests
```python
from dataclasses import dataclass

from main import Agent


@dataclass
class FakeMissionReview:
    """For testing purposes. The only relevant attribute is the grade."""
    grade: int


def test_agent_has_mission_review_list_initialized():
    agent = Agent("", "", "")

    # The mission reviews attribute
    # must be initialized to an empty list.
    assert agent.mission_reviews == []
    assert agent.calc_performance_rating() == None


def test_agent_average_less_than_five_missions():
    agent = Agent("", "", "")

    for grade in (1, 2, 3):
        review = FakeMissionReview(grade)
        agent.mission_reviews.append(review)
    
    assert agent.calc_performance_rating() == 2


def test_agent_average_exactly_five_missions():
    agent = Agent("", "", "")

    for grade in (1, 2, 3, 4, 5):
        review = FakeMissionReview(grade)
        agent.mission_reviews.append(review)
    
    assert agent.calc_performance_rating() == 3


def test_agent_average_more_than_five_missions():
    agent = Agent("", "", "")

    for grade in (0, 0, 0, 0, 5, 6, 7, 8, 9):
        review = FakeMissionReview(grade)
        agent.mission_reviews.append(review)
    
    # taking only the LAST 5 grades, the average should be 7
    assert agent.calc_performance_rating() == 7


def test_average_should_return_type_float():
    agent = Agent("", "", "")

    for grade in (1, 2):
        review = FakeMissionReview(grade)
        agent.mission_reviews.append(review)
    
    assert agent.calc_performance_rating() == 1.5
```
