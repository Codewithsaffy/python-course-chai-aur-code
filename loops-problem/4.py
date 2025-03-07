# reverse strong using loop

text = "string"
reverse_string = []
reverse_str = ""
for i in range(len(text)):
    n = (len(text)-1)-i
    reverse_string.append(text[n])

print("".join(reverse_string))


# second method to do this 

for ch in text:
    reverse_str = ch + reverse_str
print(reverse_str)