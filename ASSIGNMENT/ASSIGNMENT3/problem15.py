def merge_arrays(a, b):
    n = len(a)
    m = len(b)
    
    for i in range(n):
        if a[i] > b[0]:
            a[i], b[0] = b[0], a[i]
            first = b[0]
            
            k = 1
            while k < m and b[k] < first:
                b[k-1] = b[k]
                k += 1
            b[k-1] = first
    
    return a, b

# Example
a = [2, 4, 7, 10]
b = [2, 3]
print(merge_arrays(a, b))
