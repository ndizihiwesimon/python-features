# basic unpacking
a, b, c = [1, 2, 3]
print(f"a: {a}, b: {b}, c: {c}\n")

# extended iterable unpacking with *
a, b, *c = [1,2,3,4,5]
print(f"a: {a}, b: {b}, c: {c}\n")

# ignoring values
a, _, c = [1, 2, 3]

# unpacking with zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")


# unpacking nested structures
data = ("Alice", (25, "Engineer"))
name, (age, occupation) = data
print(f"{name} is {age} years old and works as an {occupation}.")

def bulb_switch(current_state: bool) -> bool:
    return not current_state

bulb_on = False
while True:
    data = input("Input 1 to switch: ")
    if data == "1":
        bulb_on = bulb_switch(bulb_on)
        status = "ON" if bulb_on else "OFF"
        print(f"The Bulb is: {status}")
    else:
        print(f"That's it! You pressed {data}, not 1 LoL")
        break