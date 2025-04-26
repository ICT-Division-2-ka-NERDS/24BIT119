# 24bit119

# Que-6

class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        """Overload the == operator to compare two Date objects."""
        if isinstance(other, Date):
            return (self.day == other.day and
                    self.month == other.month and
                    self.year == other.year)
        return NotImplemented

    def __str__(self):
        """Return a string representation of the date in DD-MM-YYYY format."""
        return f"{self.day:02}-{self.month:02}-{self.year}"

date1 = Date(15, 8, 2023)
date2 = Date(15, 8, 2023)
date3 = Date(1, 1, 2022)

print("Date 1:", date1)
print("Date 2:", date2)
print("Date 3:", date3)

print("Date 1 == Date 2:", date1 == date2)
print("Date 1 == Date 3:", date1 == date3)
