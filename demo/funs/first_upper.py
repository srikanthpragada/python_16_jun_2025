def first_upper(st):
    for idx, c in enumerate(st):
        if c.isupper():
            return idx

    return -1  # No uppercase found

print(first_upper('abCdA'))
print(first_upper('abb'))
