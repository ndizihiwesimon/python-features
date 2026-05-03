import itertools

# Infinite iterators
counter = itertools.count(start=12, step=2) # infinite count from 12, incrementing by 2
print(next(counter))
print(next(counter))
print(next(counter))
print("go to loop\n")

for count in counter:
    print(count)
    if count == 20:
        print("take a breath lol.")
        break

# Cycling through a finite sequence infinitely 
cycler = itertools.cycle(["A", "B", "C"])
print(next(cycler)) # A
print(next(cycler)) # B
print(next(cycler)) # C
print(next(cycler)) # A, Repeats
print(next(cycler)) # B

# creating combinations
combinations = itertools.combinations("ABC", 2)
print(list(combinations)) # Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]