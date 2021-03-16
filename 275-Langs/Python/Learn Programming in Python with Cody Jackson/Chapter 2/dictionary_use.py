language_author = {"C": "Dennis Ritchie", "Python": "Guido van Rossum", "C++": "Bjarne Stroustrup"}
language = "Python"
author = language_author[language]

for lang in language_author.keys():
    print(lang, "\t", language_author[lang])
