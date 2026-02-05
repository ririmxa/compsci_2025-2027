# Topic B2.4.1: Big O Notation & Efficiency
# CHALLENGE: This code checks if a list contains duplicates.
# It works, but it does TWICE as much work as necessary!
# 
# HINT: If we have compared element A to element B, do we need to
# compare element B to element A later? 
# Look at where the inner loop (j) starts.

#link to online Python IDE with the challenge code: https://trinket.io/python3/47b820307e0e

def has_duplicates(arr):
    comparisons = 0
    n = len(arr)
    
    # Outer loop
    for i in range(n):
        # Inner loop - BUG IS HERE
        # Why start at 0? We end up checking everything twice.
        for j in range(0, n): 
            
            # Don't compare a number to itself (e.g. index 3 vs index 3)
            if i != j:
                comparisons += 1
                if arr[i] == arr[j]:
                    print(f"List length: {n}")
                    print(f"Comparisons made: {comparisons}")
                    return True
    
    print(f"List length: {n}")
    print(f"Comparisons made: {comparisons}")
    return False

# Test Data
# A list with 10 numbers, no duplicates
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
has_duplicates(data)

# Challenge: Change the inner loop range to range(i + 1, n).
# Run it again. How did the number of comparisons change?
