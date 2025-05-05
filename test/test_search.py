import pytest
from src.search import locate_linear


tests = []

# query somewhere in the middle
tests.append({
    'input' : {
        'input' : [13, 11, 10, 7, 4, 3, 1, 0],
        'query' : 4
    },
    'output' : [4]
})

# query at the begining of the list
tests.append({
    'input' : {
        'input' : [4, 2, 1, -1],
        'query' : 4
    },
    'output' : [0]
})

# query at the end of the list
tests.append({
    'input' : {
        'input' : [3, -9, -70, -127],
        'query' : -127
    },
    'output' : [3]
})

# query in a list with one element
tests.append({
    'input' : {
        'input' : [7],
        'query' : 7
    },
    'output' : [0]
})

# query not in list
tests.append({
    'input' : {
        'input' : [7, -70, 10, 50, 8],
        'query' : 4
    },
    'output' : []
})

# list is empty
tests.append({
    'input' : {
        'input' : [],
        'query' : 4
    },
    'output' : []
})

# multiple occurences of the query
tests.append({
    'input' : {
        'input' : [10, 20, 10, 40, 7 , 10, 80, 47, 10],
        'query' : 10
    },
    'output' : [0, 2, 5, 8]
})

# numbers repeating but single occurence of the query
tests.append({
    'input' : {
        'input' : [10, 20, 10, 20, 7 , 10, 47, 7, 10],
        'query' : 47
    },
    'output' : [6]
})



@pytest.mark.parametrize('case',tests)
def test_locate(case):
    assert locate_linear(**case['input']) == case['output']