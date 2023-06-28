def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for j in range(1, n):
        previous = triangle[j - 1]
        current = [1]
        for k in range(1, j):
            current.append(previous[k - 1] + previous[k])
        current.append(1)
        triangle.append(current)

    return triangle
