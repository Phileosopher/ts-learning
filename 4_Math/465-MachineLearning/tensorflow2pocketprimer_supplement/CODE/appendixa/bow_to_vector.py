# https://nlpforhackers.io/deep-learning-introduction/

VOCAB = ['dog', 'cheese', 'cat', 'mouse']
TEXT1 = 'the mouse ate the cheese'
TEXT2 = 'the horse ate the hay'
 
def to_bow(text):
  words = text.split(" ")
  return [1 if w in words else 0 for w in VOCAB]
 
print("VOCAB: ",VOCAB)
print("TEXT1:",TEXT1)  
print("BOW1: ",to_bow(TEXT1))  # [0, 1, 0, 1]
print("")

print("TEXT2:",TEXT2)  
print("BOW2: ",to_bow(TEXT2))  # [0, 0, 0, 0]

