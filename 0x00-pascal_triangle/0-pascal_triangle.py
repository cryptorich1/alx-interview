def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if triangle:  # If there are already rows in the triangle
            prev_row = triangle[-1]  # Get the previous row
            
            # Calculate the values for the current row
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j+1])
            
            row.append(1)  # Last element of each row is always 1
        
        triangle.append(row)  # Add the current row to the triangle
    
    return triangle
