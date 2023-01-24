# https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple
from typing import List, Dict, Tuple, Union, Any, Optional

Number = Union[int, float]
OptionalInt = Optional[int]

def f(x: Number) -> Number:
    return 7 * x - 9


def transform(items: List[Number]) -> List[Number]:
    result: List[Number] = []
    for x in items:
        result.append(f(x))
    return result


def get_sum(*args: int, **kwargs: int):
    return sum(args) + sum(kwargs.values())


f1: int = f(8)
s: int = get_sum(8, 7, 9, 10, 4, 8, 13, 1, 8, 4, 9, 5, x=8, y=15)
print(s)

data: List[int] = [7, 5, 9, 4]
numbers: List[int] = transform(data)
print(*numbers) # print(40, 26, 54, 19)

info: Dict[str, int] = {'x': 8, 'y': 11}
print(get_sum(**info)) # get_sum(x=8, y=11)

person: Tuple[str, int, int] = ('Иванов И.И.', 28, 190)

random_data: Any = 10
print(random_data)
random_data = 'FESzdgfhn'
print(random_data)
random_data = None
print(random_data)
random_data = [3, 8, 5]
print(random_data)

optional: OptionalInt = 5
print(optional)
optional = None
print(optional)
optional = 6.7
print(optional)
