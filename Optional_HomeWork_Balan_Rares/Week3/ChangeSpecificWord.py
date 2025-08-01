sentence = "This is a sentence"
target_word = "this"
new_word = "that"

words = sentence.split()
modified = [new_word if word.lower() == target_word.lower() else word for word in words]
modifiedSentence = " ".join(modified)
print(modifiedSentence)
