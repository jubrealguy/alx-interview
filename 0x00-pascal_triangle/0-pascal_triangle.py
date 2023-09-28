#!/usr/bin/python3
def pascal_triangle(n):
    result = []
    for i in range(n):
        if i == 0:
            result.append([1])  # First row: [1]
        else:
            # Calculate the current row based on the previous row
            prev_row = result[-1]
            new_row = [1]
            for j in range(1, len(prev_row)):
                new_row.append(prev_row[j - 1] + prev_row[j])
            new_row.append(1)
            result.append(new_row)
    return result
