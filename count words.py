def count_words(sentence):
    words = sentence.split() #splitting the sentence
    return len(words)

# Example usage:
input_sentence = "Python programming is interesting"
word_count = count_words(input_sentence)
print("Number of words:", word_count)

# split() --> convert a string into the list

