n = 5
triangle = [[1]]
for i in range(1, n):
    row = [1]
    for j in range(1, i):
        row.append(triangle[i-1][j-1] + triangle[i-1][j])
    row.append(1)
    triangle.append(row)

pascal_triangle_dict = {}
for i in range(len(triangle)):
    pascal_triangle_dict[i] = triangle[i]

for key, value in pascal_triangle_dict.items():
    print(f'{key}: {value}')