from typing import Any, Generator, Iterator


def repeater(value: Any) -> Generator:
    while True:
        yield value


def counter(end: int) -> Generator:
    value = 0
    while value < end:
        if value >= 1000000:
            return 'Hard limit'
        value += 1
        yield value


iterator = iter(repeater(5))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# for x in repeater(5):
#     print(x)

iterator: Iterator = iter(counter(5000000000))

while True:
    try:
        x = next(iterator)
    except StopIteration as e:
        print(e)
        break
    print(x)

# for x in counter(5000000000):
#     print(x)
