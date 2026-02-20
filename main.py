# 1
text = input()
rev = ""
for c in text:
    rev = c + rev
print(rev)

# 2
text = input()
vowels = 0
for c in text.lower():
    if c in "aeiou":
        vowels += 1
print(vowels)

# 3
text = input()
words = text.split()
print(len(words))

# 4
text = input()
longest = ""
for w in text.split():
    if len(w) > len(longest):
        longest = w
print(longest)

# 5
text = input()
res = ""
for c in text:
    if c != " ":
        res += c
print(res)
