"""
Создайте transposeфункцию, которая принимает список списков и возвращает «транспонированный» список списков.
Это означает, что новый список списков должен содержать списки первого элемента из каждого списка,
второго элемента из каждого списка и т. д.

"""

matrix1 = [[1, 2], [3, 4]]
matrix2 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
csv_data = [
    ["Mary's Coffee", "3.50", "Dining"],
    ["Spirit", "187.00", "Travel"],
    ["Joe's Eats", "24.28", "Dining"],
    ["Metro", "12.00", "Travel"],
    ["Lyft", "23.45", "Travel"],
    ["Lyft", "4.00", "Travel"],
    ["Mary's Coffee", "6.75", "Dining"],
]


def transpose(args):
    return [
        list(row)
        for row in zip(*args, strict=True)
    ]


a = transpose(matrix1)
print(a)
b = transpose(matrix2)
print(b)
merchants, costs, categories = transpose(csv_data)
total_cost = sum(float(c) for c in costs)
print(total_cost)