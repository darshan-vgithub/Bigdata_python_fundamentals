import string
with open ("file_content.txt", "r") as f:
    content = f.read()
    print(content)

# Simple preprocessing
# print("my original content is :",content)

text=content
text=text.lower()
print(text)


clean_text=''
for char in text:
    if char not in string.punctuation:
        clean_text+=char

text=clean_text


words=text.split()
print(words)

print("my clean content is :",words)

for word in words:
    print(word)