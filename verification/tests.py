"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        
    {
        "input": [3, [(0, 0), (9, 8), (9, 1)]],
        "answer": 3
    },
    {
        "input": [1, [(2, 8)]],
        "answer": 4
    },
    {
        "input": [5, [(4, 4), (3, 9), (1, 8), (2, 1), (1, 2)]],
        "answer": 9
    },
    {
        "input": [10, [(0, 9), (0, 8), (0, 7), (0, 6), (0, 5), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0)]],
        "answer": 25
    }

    ]
}
