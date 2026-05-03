name: str = "Simon"
age: int = 27
is_student: bool = False

# Function annotations
def greet(person: str, age: int)-> str:
    """Greets a person by name and age

    Args:
        person (str): The name of the person (expected to be string)
        age (int): The age of the person (expected to be integer)

    Returns:
        str: A greeting message (expected to be string)
    """
    return f"Hello, {person}! You are {age} years old."


# Using the function
greeting = greet(name, age)
print(greeting)
