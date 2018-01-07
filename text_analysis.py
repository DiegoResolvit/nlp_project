from __future__ import print_function
from nltk import tokenize
import nltk, string, nltk.data, json
from nltk.stem import *
from nltk.stem.snowball import SnowballStemmer


stemmer = SnowballStemmer("english")

sentence = """Take this paragraph of text and return an alphabetized list of ALL unique words.  A unique word is any form of a word often communicated with essentially the same meaning. For example, fish and fishes could be defined as a
unique word by using their stem fish. For each unique word found in this entire paragraph, determine the how many times the word appears in total. Also, provide an analysis of what unique sentence index position or positions the word is found.
The following words should not be included in your analysis or result set: "a", "the", "and", "of", "in", "be", "also" and "as".  Your final result MUST be displayed in a readable console output in the same format as the JSON sample object shown below."""

list_of_words2 = []
list_of_words = [stemmer.stem(word.strip(string.punctuation).lower()) for word in sentence.split()]
for w in list_of_words:
    if w not in ["""""""", """''""", ":", ".", ",", """``""", "a", "the", "and", "of", "in", "be", "also", "as"]:
        list_of_words2.append(w)

list_of_words2.sort()


#punto uno del examen, obtengo mi lista sin repetidos usando el stem
unique_words = set(list_of_words2)
print("********************************************** PUNTO 1 **********************************************")
#print(sorted(unique_words))
print("********************************************** PUNTO 1 **********************************************")

tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
#tagged Imprime en pantalla el contenido del sentence_indexes

stemmer = SnowballStemmer("english")

#Recorro el objeto y muestro la lista de palabras que reconoció[0]
#for word in tagged:
#	print(word[0])

#Para saber el stem de una parala ejecuto lo siguiente
#stemmer.stem("Palabra en ingles")
#Para tener un listado de palabras y si stem hago lo siguiente
#for word in tagged:
#	print(word[0] + " " + stemmer.stem(word[0]))

#con esto tengo mi lista filtrada (sin repetidos) y la lista total, ahora tengo que
#saber cuantas ocurrencias de cada palabra tengo en el texto.

#creo mi colección de palabras y su respectivo stem, desde el texto original
pos = {}
for word in tagged:
    if stemmer.stem(word[0]) not in ["""""""", """''""", ":", ".", ",", """``""", "a", "the", "and", "of", "in", "be", "also", "as"]:
        pos[word[0]] = stemmer.stem(word[0])
        #print(word[0] + "-------------" + stemmer.stem(word[0]))
    


#Recorro la lista de palabras ordenada y contabilizo en base al texto original
#Este es el punto 2 del examen, tener la lista y pasarle la cantidad de ocurrencias.
i = 0
total_occurrences = {}
print("********************************************** PUNTO 2 **********************************************")
for word in sorted(unique_words):
    for keyWord in tagged:
        if stemmer.stem(word) == stemmer.stem(keyWord[0]):
           i = i + 1
    total_occurrences[stemmer.stem(word)] = i
    # print(word + " Cantidad: " + str(i))
    i = 0
print("********************************************** PUNTO 2 **********************************************")
#para hacer mañana, tengo el texto separado en palabras que ya estan stemeadas y tengo que encontar donde la uso poniendo el número de oración y la posición de la palabra
#    def all_occurences(sentence, str):
#    initial = 0
#    while True:
#        initial = sentence.find(str, initial)
#        if initial == -1: return
#        yield initial
#        initial += len(str)
# usar la función anterior para pasarle la oración y que me devuelva los indices de donde está la palabra.
# lista tokenizada de palabras del párrafo --> nltk.word_tokenize(stemmer.stem(sentence))
# con la lista anterior más la de sentencias busco los donde (oración) y posición (indice en oración) de cada palabra.        
# me devuelve las posiciones de las palabras --> [i for i, item in enumerate(nltk.word_tokenize(stemmer.stem(sentences[6]))) if item == 'the']


#revisar este código, no me está devolciendo correctamente la info como yo quiero. el print funciona pero tengo que ver como exporto la info
#este es el punto 3 del examen, saber en que párrafo y posición está cada palabra.
sentences = tokenize.sent_tokenize(sentence)    
i = 0
x = 0
sentence_indexes = {}
y = 0

print("********************************************** PUNTO 3 **********************************************")
for word in sorted(unique_words):
    lista2 = []
    #print("Palabra: " + word)
    for single_sentence in sentences:
        lista = [w for w, item in enumerate(nltk.word_tokenize(single_sentence)) if stemmer.stem(item) == stemmer.stem(word)]
        if len(lista) > 0:
            #pass
            #print(" Parrafo: " + str(y))
            #i += len(lista)
            lista2.append(y)
        y += 1
    sentence_indexes[stemmer.stem(word)] = lista2
    i = 0
    y = 0
    #print(sentence_indexes)
print("********************************************** PUNTO 3 **********************************************")

strjson = { 'results': [{ 'word': a, 'sentence-indexes': sentence_indexes[a], 'total-occurrences': total_occurrences[a] } for a in sorted(unique_words)]}
print(json.dumps(strjson))

#print(list_of_words)
#print("\n\r")
#print(sorted(unique_words))
