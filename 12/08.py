# 24bit119

# Que-8

class String:
    def __init__(self, value=""):
        self.value = value

    def __iadd__(self, other):
        """Overload the += operator for string concatenation."""
        if isinstance(other, String):
            self.value += other.value
        elif isinstance(other, str):
            self.value += other
        else:
            return NotImplemented
        return self

    def toLower(self):
        """Convert the string to lowercase."""
        self.value = self.value.lower()

    def toUpper(self):
        """Convert the string to uppercase."""
        self.value = self.value.upper()

    def __str__(self):
        """Return the string representation of the object."""
        return self.value

str1 = String("Hello")
str2 = String(" World")

print("Initial String 1:", str1)
print("Initial String 2:", str2)

str1 += str2
print("After concatenation:", str1)

str1.toLower()
print("After converting to lowercase:", str1)

str1.toUpper()
print("After converting to uppercase:", str1)
