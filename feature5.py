def my_decorator(func):
    """Decorator that prints message before and after running the function

    Args:
        func (func): the function that says hello
    """
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@my_decorator
def say_hello(name: str):
    """Function that greets the user
    """
    print("Hello Simon!")


if __name__ == "__main__":
    say_hello("Simon")