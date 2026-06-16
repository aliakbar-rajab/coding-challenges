class Vector:
    def __init__(self, coordinates: list):
        self.values = coordinates
        
    def _check_length(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must have the same length!")
​
    def add(self, other):
        self._check_length(other)
        new_coords = [a + b for a, b in zip(self.values, other.values)]
        return Vector(new_coords)
​
    def subtract(self, other):
        self._check_length(other)
        new_coords = [a - b for a, b in zip(self.values, other.values)]
        return Vector(new_coords)
​
    def dot(self, other):
        self._check_length(other)
        return sum(a * b for a, b in zip(self.values, other.values))
​
    def norm(self):
        return sum(x**2 for x in self.values) ** 0.5
​
    def equals(self, other):
        return self.values == other.values
​
    def __str__(self):
        joined_numbers = ",".join(str(val) for val in self.values)
        return f"({joined_numbers})"