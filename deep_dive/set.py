s = {}        # This is a DICT, not a set!
s = set()     # ✅ Correct way to make empty set


s.add(4)
s.remove(2)       # Throws error if 2 not found
s.discard(5)      # Safer remove – no error if 5 not found
s.clear()         # Removes everything
