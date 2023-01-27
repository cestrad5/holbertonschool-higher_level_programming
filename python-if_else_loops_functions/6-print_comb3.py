#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if a != b and a < b:
            print(f"{a}{b}", end="")
            if a != 8:
                print(", ", end="")
print()
