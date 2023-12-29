import sys

sys.setrecursionlimit(10**6)  # Set the recursion limit to a higher value

def are_equivalent_strings(a, b):
    if a == b:
        return True
    
    n = len(a)
    if n == 1: return False
    
    # Check condition a1 is equivalent to b1, and a2 is equivalent to b2
    if (are_equivalent_strings(a[:n // 2], b[:n // 2]) and
            are_equivalent_strings(a[n // 2:], b[n // 2:])):
        return True

    # Check condition a1 is equivalent to b2, and a2 is equivalent to b1
    if (are_equivalent_strings(a[:n // 2], b[n // 2:]) and
            are_equivalent_strings(a[n // 2:], b[:n // 2])):
        return True

    return False

# Input
a = input().strip()
b = input().strip()

# Output
result = "YES" if are_equivalent_strings(a, b) else "NO"
print(result)