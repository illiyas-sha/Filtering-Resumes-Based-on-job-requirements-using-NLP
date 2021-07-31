from nltk.stem.wordnet import WordNetLemmatizer             #Word tokenize as well as parts of speech tag are imported from nltk
from sklearn.feature_extraction.text import CountVectorizer #Convert a collection of text documents to a matrix of token counts
from nltk.corpus import stopwords                           #for removing predefined stop words in english
from preprocessing import lemma_tag as tag               #for taging words pos


#initialising wordnet Lemmatizer
lemmatizer = WordNetLemmatizer()

#converting text into matrix
analyser = CountVectorizer().build_analyzer()

def stemmed_words(doc):

    #Lemmatize Sentence with the appropriate POS tag
    return (lemmatizer.lemmatize(word,tag.get_wordnet_pos(word))for word in analyser(doc) if word not in set(stop_words.words('english')))
