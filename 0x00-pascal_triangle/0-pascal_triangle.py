#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    
    ptriangle = []
    
    for i in range(n):
        row = [1]
        if ptriangle:
            prev_row = ptriangle[-1]
            
            # Calculate the values for the current row
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j+1])
            
            row.append(1)
        
        ptriangle.append(row)
    
    return ptriangle
