text = 'abcdefghijklmnop'

for letter in text:
    print(letter)

i = 0
while i < len(text):
    print(text[i])
    i += 1

# jumping 1 character

i = 0
while i < len(text):
    print(text[i])
    i += 2

# to print backwards
# method 1
i = len(text) - 1
while i >= 0:
    print(text[i], end="")
    i -= 1

# method 2

i = 0
while i < len(text):
    print(text[len(text)-i-1], end="")
    i += 1

# jumping 1 character

i = len(text) - 1
while i >= 0:
    print(text[i], end="")
    i -= 2