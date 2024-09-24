"""
Я хочу, чтобы вы написали функцию, которая принимает итерируемый объект и возвращает новый
итерируемый объект со всеми элементами исходного итерируемого объекта, за исключением дубликатов.
Обратите внимание, что порядок возвращаемых элементов должен остаться прежним.
"""


def uniques_only(numbers):
    seen = set()
    items = []
    for item in numbers:
        if item not in seen:
            items.append(item)
            seen.add(item)
    return items


# или просто:
# return list(dict.fromkeys(numbers))

result = uniques_only([1, 2, 2, 1, 1, 3, 2, 1])
print(result)

nums = [1, -3, 2, 3, -1]
squares = (n ** 2 for n in nums)
print(uniques_only(squares))
