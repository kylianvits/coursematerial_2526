# write your code here
# student.py

# Strategy 1 — Replace all A’s with o’s
def decode1(word):
    return word.replace("A", "o")


# Strategy 2 — Every second letter is random → keep every 2nd character (index 0, 2, 4, ...)
def decode2(word):
    return word[::2]


# Strategy 3 — The first word in the sentence is reversed
def decode3(sentence):
    words = sentence.split(" ")
    if not words:
        return sentence
    words[0] = words[0][::-1]  # reverse first word
    return " ".join(words)


# Strategy 4 — The original word is hidden starting at the 3rd letter
# and is half as long as the encrypted word.
def decode4(word):
    # Start at index 2 (third letter), take half of total length
    half_len = len(word) // 2
    return word[2:2 + half_len]
