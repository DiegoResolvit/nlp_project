from __future__ import print_function
from nltk import tokenize
import nltk, string, nltk.data, json
from nltk.stem import *
from nltk.stem.snowball import SnowballStemmer


stemmer = SnowballStemmer("english")
#para no tener que correrlo por afuera
nltk.download('punkt')

#párrafo que tengo que trabajar
sentence = """Take this paragraph of text and return an alphabetized list of ALL unique words.  A unique word is any form of a word often communicated with essentially the same meaning. For example, fish and fishes could be defined as a
unique word by using their stem fish. For each unique word found in this entire paragraph, determine the how many times the word appears in total. Also, provide an analysis of what unique sentence index position or positions the word is found.
The following words should not be included in your analysis or result set: "a", "the", "and", "of", "in", "be", "also" and "as".  Your final result MUST be displayed in a readable console output in the same format as the JSON sample object shown below."""

#Filtro la la black List

list_of_filtered_words = []
list_of_words = [stemmer.stem(word.strip(string.punctuation).lower()) for word in sentence.split()]
black_list = ["""""""", """''""", ":", ".", ",", """``""", "a", "the", "and", "of", "in", "be", "also", "as"]

list_of_filtered_words = [x for x in list_of_words if x not in black_list]
list_of_filtered_words.sort()


#punto uno del examen, obtengo mi lista sin repetidos usando set
unique_words = set(list_of_filtered_words)

#separo las palabras
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

#seteo el stemmer a ingles
stemmer = SnowballStemmer("english")

#Recorro la lista de palabras ordenada y contabilizo en base al texto original
#Este es el punto 2 del examen, tener la lista y pasarle la cantidad de ocurrencias.

i = 0
total_occurrences = {}
for word in sorted(unique_words):
    for keyWord in tagged:
        if stemmer.stem(word) == stemmer.stem(keyWord[0]):
           i = i + 1
    total_occurrences[stemmer.stem(word)] = i
    i = 0

sentences = tokenize.sent_tokenize(sentence)    

sentence_indexes = {}
y = 0

#Creo mi lista de indices de oraciones.
for word in sorted(unique_words):
    lista2 = []
    for single_sentence in sentences:
        lista = [w for w, item in enumerate(nltk.word_tokenize(single_sentence)) if stemmer.stem(item) == stemmer.stem(word)]
        if len(lista) > 0:
            lista2.append(y)
        y += 1
    sentence_indexes[stemmer.stem(word)] = lista2
    y = 0

strjson = { 'results': [{ 'word': a, 'sentence-indexes': sentence_indexes[a], 'total-occurrences': total_occurrences[a] } for a in sorted(unique_words)]}
print(json.dumps(strjson))
