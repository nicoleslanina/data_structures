def mergeSortString(s):
    if len(s) <= 1: # Base case: string of length 0 or 1 
        return s

    # Split the string into two halves
    mid = len(s) // 2
    left = mergeSortString(s[:mid])
    right = mergeSortString(s[mid:])

    # Merge sorted halves
    return merge(left, right)

def merge(left, right):
    result = ""
    i = j = 0

    # Merge two sorted strings
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result += left[i]
            i += 1
        else:
            result += right[j]
            j += 1

    # Append remaining characters
    result += left[i:]
    result += right[j:]

    return result

# trying the example
input_str = 'louisa'
sorted_str = mergeSortString(input_str)
print(sorted_str)  # Output: 'ailosu'
