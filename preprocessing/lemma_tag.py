import nltk
from nltk.corpus import wordnet
def get_wordnet_pos(word):
    """Mapping POS tag to first character lemmatize() accepts"""
    nltk_tag = nltk.pos_tag([word])[0][1][0].upper()
    lemmatizer_tag_dict =  {"J": wordnet.ADJ,
                            "N": wordnet.NOUN,
                            "V": wordnet.VERB,
                            "R": wordnet.ADV}
    return lemmatizer_tag_dict.get(nltk_tag, wordnet.NOUN)