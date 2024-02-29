text = "0123456789abcdef"

# to slice 5678
print(text[5:9])

# to print 0123456789
print(text[0:10])
# or just:
print(text[:10])

# to print abcdef
print(text[10:])
# or:
print(text[-6:])

# to print 02468ace (skipping characters)
print(text[::2])

# skipping characters but not starting from the 0
print(text[1::2])

# backwards
print(text[::-1])