from collections import Counter 

mywords = ['a', 'b', 'a', 'b', 'c', 'a', 'd', 'e', 'f', 'b']

word_counts = Counter(mywords)
topThree = word_counts.most_common(3) 
print(topThree)

