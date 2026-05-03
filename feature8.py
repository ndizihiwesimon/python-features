def count_up_to(max_value: int):
    """A generator method that yield numbers from 1 to max_value

    Args:
        max_value (int): Max value
    """
    current = 1
    while current <= max_value:
        yield current # Yield the current value and pause execution
        current +=1 # increment the current value

if __name__ == "__main__":
    counter = count_up_to(1000000)

    for count in counter:
        print(f"{count:,}")