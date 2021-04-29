from .utils import calc_difficulty, flatten_concepts

# concept -> prerequisets

concepts = {
    "introduction to programming": {
        "output a message": [],
        "mathematical operations": [],
        "storing data in variables": [],
        "format output text": [
            "output a message",
            "storing data in variables"],
        "get input from the user": [
            "output a message",
            "storing data in variables"],
        "convert strings to numbers": [
            "get input from the user"],
    },
    "strings": {
        "string concatenation": [],
        "access a single character": [],
        "substrings and slicing": [
            "access a single character"],
        "convert to lower/upper case": [],
        "replace characters or substrings": [],
        "split a string into a list": []
    },
    "if statements": {
        "boolean values in variables": [],
        "comparison operators": [],
        "if, else": ["comparison operators"],
        "if, elif, else": ["if, else"],
        "multiple elif": ["if, elif, else"],
        "boolean operators": ["if, else"]
    },
    "loops": {
        "loop with a counter variable": [
            "storing data in variables",
            "mathematical operations"
        ],
        "loop with an accumulator variable": ["loop with a counter variable"],
        "break": ["loop with a counter variable", "if, else"],
        "continue": ["loop with a counter variable", "if, else"],
        "get user input in a loop": [
            "get input from the user",
            "loop with an accumulator variable"],
        "quit loop with sentinel value": [
            "get user input in a loop",
            "break"],
        "loop through a string (while)": [
            "loop with a counter variable",
            "access a single character"],
        "loop through a list (while)": [
            "accessing list elements",
            "loop with a counter variable"],
        "loop using range": ["loop with a counter variable"],
        "loop using enumerate": ["loop using range"],
        "loop through a string (for)": ["loop through a string (while)"],
        "loop through a list (for)": ["loop through a list (while)"],
        "string building and filtering": [
            "string concatenation",
            "if, else",
            "loop with an accumulator variable",
            "loop through a string (for)"]
    },
    "lists": {
        "creating a list": [],
        "accessing list elements": [],
        "slicing a list": ["accessing list elements"],
        "appending elements to a list": [],
        "reassign element at list index": ["accessing list elements"],
        "remove list element using .remove": [],
        "remove list element at index using del": ["accessing list elements"],
        "insert element at index": ["accessing list elements"],
        "append user input to a list using a loop": [
            "appending elements to a list",
            "get user input in a loop",],
        "check if a value is in a list": [
            "loop through a list (for)",
            "if, else"],
        "find the largest item in a list": [
            "loop through a list (for)",
            "loop with an accumulator variable",
            "if, else"],
        "list building and filtering": [
            "appending elements to a list",
            "if, else",
            "loop with an accumulator variable",
            "loop through a list (for)"]
    },
    "exceptions": {},
    "functions": {
        "calling a function": [],
        "passing arguments": [
            "calling a function"
        ],
        "handling return values": [
            "calling a function"
        ],
        "defining a function": [
            "calling a function"
        ],
        "returning a value": [
            "handling return values",
            "defining a function"
        ],
        "defining parameters": [
            "defining a function",
            "returning a value",
            "passing arguments"
        ],
        "docstrings": [
            "defining parameters",
            "defining a function",
            "returning a value"
        ]
    },
    "testing": {},
    "dictionaries": {
        "creating a dictionary": [],
        "accessing a value in a dictionary": [
            "creating a dictionary",
        ],
        "adding a value to a dictionary": [
            "creating a dictionary",
        ],
        "modifying a value in a dictionary": [
            "accessing a value in a dictionary",
        ],
        "removing a value in a dictionary": [
            "accessing a value in a dictionary",
        ],
        "iterating through dictionary keys": [
            "loop through a list (for)",
            "accessing a value in a dictionary",
        ],
        "iterating through dictionary values": [
            "loop through a list (for)",
            "accessing a value in a dictionary",
        ],
        "iterating through dictionary keys and values": [
            "iterating through dictionary keys",
            "iterating through dictionary values",
        ],
    },
    "file r/w": {
        "read from a file": [],
        "read multiple lines from a file": [
            "loop through a list (for)",
            "read from a file"
        ],
        "write to a file": [],
        "append to a file": [
            "write to a file"
        ],
        "write multiple lines to a file": [
            "loop through a list (for)",
            "write to a file"
        ],
        "load json data from a file": [
            "read from a file"
        ],
        "write json data to a file": [
            "write to a file"
        ]
    },
    "classes": {
        "docstrings (classes)": []
    },
    "algorithms": {}
}



# concept_difficulties = []
# flat_concepts = flatten_concepts(concepts)
# for concept, requirements in flat_concepts.items():
#     concept_difficulties.append((concept, calc_difficulty(requirements, concepts)))

