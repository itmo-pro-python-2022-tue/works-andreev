def f(x):
    return 7 * x - 9


def transform(items):
    result = []
    for x in items:
        result.append(f(x))
    return result


def get_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


print(get_sum(8, 7, 9, 10, 4, 8, 13, 1, 8, 4, 9, 5, x=8, y=15))

data = [7, 5, 9, 4]
numbers = transform(data)
print(*numbers) # print(40, 26, 54, 19)

info = {'x': 8, 'y': 11}
print(get_sum(**info)) # get_sum(x=8, y=11)
