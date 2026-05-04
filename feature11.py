students=[{
    "name": "Nomiso",
    "age": 27,
    "country": "Rwanda",
    "phone_model": "iPhone 13 Mini",
    "address": "Kigali, RW"
},
{
    "name": "Sandra",
    "age": 23,
    "country": "Rwanda",
    "phone_model": "iPhone 13",
    "address": "Nairobi, KE"
},
]

# construct a new list with list comprehension 
new_students=[{key.upper(): value for key, value in student.items()} for student in students]

def display(items: list):
    """
    Displaying JSON keys and values before renaming keys.
    """
    print("Keys before")
    print("-"*12)
    for i, item in enumerate(items):
        print(f"\nStudent {i}:")
        for key, value in item.items():
            print(f"Key: {key}, value: {value}")

def rename(items: list):
    """
    The method renames dict keys in place, by popping the item from the dict.
    """
    print("\nKeys after:")
    print("-"*12)
    for item in items: 
        for key in list(item.keys()):
            item[key.upper()] = item.pop(key)
    
    for item in items:
        for key, value in item.items():
            print(f"Key: {key}, value: {value}")
        
        print("\n")

if __name__ == "__main__":
    display(items=students)
    rename(students)
    display(new_students)