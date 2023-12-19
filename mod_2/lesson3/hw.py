pascal_triangle = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1]
]

pascal_triangle_dict = {}

for i,j in enumerate(pascal_triangle):
    pascal_triangle_dict[i] = j

print(pascal_triangle_dict)
