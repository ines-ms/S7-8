text = "abcdefghijklmnop"
print(dir(text))
help(text.isupper())
print(text.isupper())  # is the text in uppercase?
print("ABC".isupper())  # is the text all uppercase?
print(text.upper())  # convert the text to uppercase
print(text.upper().isupper())  # is the text all uppercase? yes

new_text = text.upper()
print(text, new_text)

# .count function
print("bannannana" .count("n"))  # to count the amount of times n appears in the text

# .index function
print("banababababnan" .index("b"))  # which position is b found in
print("banabaababana" .index("ana"))  # which pos does ana start

# .replace function
print("bananabnabnabdnana" .replace("ana", "XXYYZZ"))  # replace ana with XXYYZZ

#  give the sentence without all the punctuation
sentence = "Hello, kind-sir; how may! I be of service today?"
punctuation = ".,;!?-"  # define punctuation first
for p in punctuation:
    sentence = sentence.replace(p, "")  # replace values with nothing
print(sentence)

# cut the string into pieces every time there is a space-> result is a list of strings
print("this is a sentence and I want the words" .split(" "))

text = "Bob goes to school. Bob likes to play tennis. I am friends with Bob. Such a nice guy Bob is."
# print(text.find("Bob"))
# print(text.rfind("Bob"))
# find each position in which Bob is
i = 0
while i < len(text):
    i = text.find("Bob", i)
    if i == -1:
        break
    print(i)
    i += 1