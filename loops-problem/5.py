# find the first non-repeated charachter

text = "hello"

for i in text:
    if text.count(i) > 1:
        print(i)
        break

    