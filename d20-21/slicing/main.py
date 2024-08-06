piano_keys = ["a", "b", "c", "d", "e", "f", "g"]


# want to get c d e
print(piano_keys[2:5])

# want to get everything from c
print(piano_keys[2:])

# want to get only c and e (it takes first c to e then only takes every SECOND item in that slice)
print(piano_keys[2:5:2])

# want to get the list reversed
print(piano_keys[::-1])

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print(piano_tuple[2:5])
print(piano_tuple[2:])
print(piano_tuple[2:5:2])
print(piano_tuple[::-1])