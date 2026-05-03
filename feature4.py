class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        """Return a string representation of the Person object."""

        return f"Person(name={self.name!r}, age={self.age})"
    
    def __str__(self) -> str:
        """Return a user-friendly string representation of the Person object."""

        return f"{self.name} is {self.age} years old."
    
# Create a Person object
person = Person("Alice", 30)
# Print the object using __repr__
print(repr(person))
# Print the object using __str__
print(str(person))
