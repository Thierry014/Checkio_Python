from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
    return True if items == sorted(items) and len(items) == len(set(items)) else False



print(is_ascending([1,2,3]))