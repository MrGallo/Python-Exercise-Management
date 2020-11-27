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
        "get a single character": [],
        "substrings and slicing": [
            "get a single character"],
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
        "loop with a counter variable": ["storing data in variables"],
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
            "get a single character"],
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
        "count words that start/end with a substring": [
            "loop through a list (for)",
            "substrings and slicing",
            "if, else",
            "loop with an accumulator variable"],
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
        ]
    },
    "testing": {},
    "dictionaries": {},
    "file r/w": {},
    "classes": {},
    "algorithms": {}
}



# concept_difficulties = []
# flat_concepts = flatten_concepts(concepts)
# for concept, requirements in flat_concepts.items():
#     concept_difficulties.append((concept, calc_difficulty(requirements, concepts)))

