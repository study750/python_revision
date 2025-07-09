a = [1, 2, 3]
b = list("abc")              # ['a', 'b', 'c']
c = [0] * 5                  # [0, 0, 0, 0, 0]
d = list(range(5))           # [0, 1, 2, 3, 4]


a[0]         # First element
a[-1]        # Last element
a[1:3]       # Slice index 1 to 2
a[:3]        # First 3 elements
a[::2]       # Every 2nd element
a[::-1]      # Reverse the list


a.append(x)         # Add x to end
a.insert(i, x)      # Insert x at index i
a.extend([x, y])    # Add multiple values


a.remove(x)      # Remove first occurrence of x
a.pop()          # Remove last element
a.pop(i)         # Remove element at index i
del a[i]         # Delete item at index i
a.clear()        # Remove all elements


x in a           # Check if x exists
a.index(x)       # Get index of x
a.count(x)       # Count how many times x appears


for x in a: ...
for i, val in enumerate(a): ...


a.sort()                     # Sort ascending (in-place)
a.sort(reverse=True)         # Descending
a.sort(key=len)              # Custom sort
sorted(a)                    # Returns new sorted list

a.reverse()                  # In-place reverse
reversed(a)                  # Returns an iterator


[x**2 for x in a]                     # Transformation
[x for x in a if x % 2 == 0]          # Filtering
[x if x % 2 == 0 else 0 for x in a]   # Conditional


b = a.copy()             # Shallow copy
b = a[:]                 # Shallow copy
b = list(a)              # Another shallow copy


len(a)           # Length of list
sum(a)           # Sum of elements
min(a), max(a)   # Smallest / largest
list(set(a))     # Remove duplicates
