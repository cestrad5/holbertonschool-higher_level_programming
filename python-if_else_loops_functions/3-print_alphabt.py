#!/usr/bin/python3
for a_to_z in range(ord('a'), ord('z') + 1):
    if chr(a_to_z) not in ['e', 'q']:
        print("{}".format(chr(a_to_z)), end="")
