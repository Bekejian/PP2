sentence=(input())
def reverse_sen(sentence):
    words=sentence.split()              # words is a list here to store many value(words)
    return " ".join(reversed(words))
print(reverse_sen(sentence))

