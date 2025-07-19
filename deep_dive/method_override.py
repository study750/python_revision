# Class Maester with write() → prints "Recording history..."

# Class Archmaester inherits from Maester
# → overrides write() to also say: "Preserving ancient scrolls."

# Use super().write() + your own line.

class master:
   def write(self):
     print("recording history")

class archmaster(master):
   def write(self):
      super().write()
      print("perserving ")

me=archmaster()
me.write()