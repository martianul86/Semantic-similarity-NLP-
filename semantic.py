import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("car")
word2 = nlp("driver")
word3 = nlp("dog")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))



nlp = spacy.load('en_core_web_sm')
word1 = nlp("car")
word2 = nlp("driver")
word3 = nlp("dog")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Found that the simple model can distinguish less connections between words
# The simple model is doing direct connections as is using context-sensitive tensors