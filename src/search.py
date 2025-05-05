from typing import List

def locate_linear(input: List[int], query: int) -> List[int]:
    """Searches linearly for the specified query within the input list and returns the list of index of its occurrences.

    Args:
        input (List[int]):  The list to search through
        query (int): The number to search for in the list.

    Returns:
        List[int]: The list index of the occurrences of the query  in the list. An empty list is returned, if the query is not present
                    or the list is empty.
    """

    
    index = [] #list to store the indices
    
    for i,num in enumerate(input):

        if num == query:
            index.append(i)

    return index




    