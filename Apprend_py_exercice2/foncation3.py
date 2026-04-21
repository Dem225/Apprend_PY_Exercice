def count_words(sentence):
    sentence=str(sentence)
    return len(sentence.split())

print(count_words("Bonjour tout le monde"))