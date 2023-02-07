from typing import List, Iterator, Any


class Repeater:
    def __init__(self, value: Any):
        self.value: Any = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


class Counter:
    def __init__(self, end: int):
        self.end: int = end
        self.value: int = 0

    def __iter__(self):
        self.value: int = 0
        return self

    def __next__(self):
        if self.value >= self.end:
            print('Raising StopIteration')
            raise StopIteration
        self.value += 1
        return self.value


# data: List[int] = [8, 1, 4]
# data = Repeater(5)
data = Counter(5)

for x in data:
    print(x)

for x in data:
    print(x)

# iterator: Iterator = iter(data)
#
# while True:
#     try:
#         x = next(iterator)
#     except StopIteration:
#         break
#     print(x)
