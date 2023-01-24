def f(x: int) -> int:
    return 7 * x - 9


def transform(items: list) -> list:
    result: list = []
    for x in items:
        result.append(f(x))
    return result


def get_sum(*args: int, **kwargs: int):
    return sum(args) + sum(kwargs.values())


f1: int = f(8)
s: int = get_sum(8, 7, 9, 10, 4, 8, 13, 1, 8, 4, 9, 5, x=8, y=15)
print(s)

data: list = [7, 5, 9, 4]
numbers: list = transform(data)
print(*numbers) # print(40, 26, 54, 19)

info: dict = {'x': 8, 'y': 11}
print(get_sum(**info)) # get_sum(x=8, y=11)
