# 24bit119

# Que-5

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def normalize(self):
        """Normalize the time to ensure minutes and seconds are within their respective ranges."""
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60
        if self.hours < 0 or self.minutes < 0 or self.seconds < 0:
            raise ValueError("Time values cannot be negative.")

    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Time):
            total_seconds_self = self.to_seconds()
            total_seconds_other = other.to_seconds()
            return Time.from_seconds(total_seconds_self - total_seconds_other)
        return NotImplemented

    def to_seconds(self):
        """Convert the time to total seconds."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        """Create a Time object from total seconds."""
        if total_seconds < 0:
            raise ValueError("Total seconds cannot be negative.")
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)

    def __str__(self):
        """Return a string representation of the time in HH:MM:SS format."""
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

time1 = Time(1, 30, 45)
time2 = Time(0, 45, 30)
print("Time 1:", time1)
print("Time 2:", time2)

time_sum = time1 + time2
print("Sum of Time 1 and Time 2:", time_sum)

time_diff = time1 - time2
print("Difference of Time 1 and Time 2:", time_diff)

try:
    time_negative = time2 - time1
    print("Negative Time:", time_negative)
except ValueError as e:
    print("Error:", e)
