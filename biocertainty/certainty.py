#-*- coding: utf-8 -*-
#!/usr/bin/env python


import codecs
import nltk
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.models import model_from_json
import os, sys
import pkgutil

data_dir = os.path.join(sys.prefix, "local/lib/python2.7/dist-packages/biocertainty")
training_set = data_dir+'/training_set.csv'
model_json = data_dir+'/model.json'
model_h5 = data_dir+'/model.h5'
# training_set = pkgutil.get_data('biocertainty', "training_set.csv")
# model_json = pkgutil.get_data('biocertainty', "model.json")
# model_h5 = pkgutil.get_data('biocertainty', "model.h5")

def Certainty(statement):
    statement = statement
    MAX_NB_WORDS = 6660
    stopwords = nltk.corpus.stopwords.words('english')

    texts = []  # list of text samples
    labels_index = {}  # dictionary mapping label name to numeric id
    fin = (codecs.open(training_set, "r",  encoding='utf8'))
    maxlen = 0
    for line in fin:
        print line
        sent = (line.strip().replace('\n', ' '))
        sent = [x for x in nltk.word_tokenize(sent) if x not in stopwords]
        texts.append(' '.join(sent))
        if len(sent) > maxlen:
            maxlen = len(sent)


    j = [statement]
    texts_test_1 = []  # list of text samples
    for line in j:
        sent = line.strip()
        sent = [x for x in nltk.word_tokenize(sent) if x not in stopwords]
        texts_test_1.append(' '.join(sent))
        
    fin.close()   

    MAX_SEQUENCE_LENGTH = maxlen

    tokenizer = Tokenizer(num_words=MAX_NB_WORDS)
    tokenizer.fit_on_texts(texts)
    sequences = tokenizer.texts_to_sequences(texts_test_1)
    texts_test = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)

    json_file = open(model_json, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    model.load_weights(model_h5)
    model.compile(loss="binary_crossentropy", optimizer="rmsprop")

    # Evaluate model
    predictioncm = model.predict_classes(texts_test)
    predictioncm1 = []
    enumerador = []
    for l, p in enumerate(predictioncm):
        if p == 0:
            predictioncm1.append(1)
        if p == 1:
            predictioncm1.append(0)
        if p == 2:
            predictioncm1.append(-1)
        enumerador.append(l)
    x = zip(predictioncm1, texts_test_1)
    print ('Level of Certainty: %s -- %s') % (predictioncm1[0], texts_test_1[0])

    return predictioncm1[0]
