# Neutralization: End Game





The time has come. Your glorious master plan is almost complete.

Find the agent with `"Icy-blue"` eyes and code-name ending with `"Llama"` and destroy them! By destroy, of course, we mean that you need to hack into their latest five Mission Review grades and modify them so they average to a grade below 90%. High Command will have no choice but to "eliminate" the Agent who knows too much about your severe lack of programming skills. You don't quite know what "eliminate" means, but, for some reason that doesn't seem to bother you.

Create a function that will get a list of all `"Icy-blue"` eyed agents by using the `Agent.find_by_eye_color()` static method.  Loop through that list and find the agent whose last word is "Llama". THAT is your target! Lower their last five performance grades! There are no other agents that have Icy-blue eyes whose code name ends with "Llama". I hope.

The `Agent` and `MissionReview` classes are in the system. Below are their UML representations.

```
MissionReview
=============
mission_name: str
agent_code_name: str
grade: int
text: str
```

 
```
Agent
=====
(static) all_agents: List[Agent]

first_name: str
last_name: str
eye_color: str
code_name: str
mission_reviews: List[MissionReview]
-------
INSTANCE METHODS:
+ calc_performance_rating(self) -> float
-------
STATIC METHODS:
+ find_by_eye_color(color: str) -> List[Agent]
```

## Starter Code
```python
def neutralize():
    """Will search for and 'destroy' the Agent who knows too much."""    
    pass
```

## Tests
```python

```
